
TRACK_ID=PS8

# Supply Chain Disruption Response Assistant

## Problem
This application helps distributors understand supplier disruptions and identify their impact on shipments, inventory, and customer orders.

## Features
- Gemini-based disruption analysis
- Product identification
- Affected shipment detection
- Inventory impact analysis
- Shortage calculation
- Affected customer identification
- Customer order urgency ranking
- Recommended response actions

## Technology
- Python
- Flask
- Pandas
- Google Gemini

## How to Run

Install the required packages:

pip install -r requirements.txt

Start the application:

python app.py

Open the application in a browser:

http://127.0.0.1:8000

## Example
Enter a supplier disruption notice such as:

ABC Electronics has stopped production of Phone Display because of a manufacturing problem. The disruption is expected to last for 7 days.

The system analyzes the notice and identifies affected shipments, inventory, shortages, and customer orders.