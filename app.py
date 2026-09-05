from flask import Flask, render_template, request
import pandas as pd
from google import genai

app = Flask(__name__)

client = genai.Client()

shipments = pd.read_csv("data/shipments.csv")
inventory = pd.read_csv("data/inventory.csv")
orders = pd.read_csv("data/orders.csv")


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        notice = request.form["notice"]

        prompt = f"""
        Read this supply-chain disruption notice:

        {notice}

        Identify the product affected.
        Return ONLY the product name.
        """

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )

        product = response.text.strip()

        affected_shipments = shipments[
            shipments["product"].str.lower() == product.lower()
        ]

        affected_inventory = inventory[
            inventory["product"].str.lower() == product.lower()
        ]

        affected_orders = orders[
            orders["product"].str.lower() == product.lower()
        ]
        

        total_demand = affected_orders["quantity"].sum()
        available_stock = affected_inventory["quantity"].sum()
        shortage = max( total_demand - available_stock,0)
        affected_orders = affected_orders.sort_values("due_date")
        affected_orders = affected_orders.sort_values("due_date")

        for i, row in affected_orders.iterrows():
            if row["due_date"] == affected_orders["due_date"].min():
                urgency = "HIGH"
            elif row["due_date"] == affected_orders["due_date"].max():
                urgency = "LOW"
            else:
                urgency = "MEDIUM"

            affected_orders.loc[i, "urgency"] = urgency



        result = {
            "product": product,
            "shipments": affected_shipments.to_dict("records"),
            "stock": available_stock,
            "orders": affected_orders.to_dict("records"),
            "demand": total_demand,
            "shortage": shortage
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)