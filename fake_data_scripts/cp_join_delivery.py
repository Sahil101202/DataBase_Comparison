import json
import random

# Load customers data from JSON file
with open('customer_product_join(0.25M).json', 'r') as f:
    carts = json.load(f)

# Load electronic products data from JSON file
with open('delivery_companies(0.25M).json', 'r') as f:
    company = json.load(f)

# Randomly assign electronic products to customers
for cart in carts:
    cart['delivery_company'] = random.choices(company)

# Save joined data to JSON file
with open('customer_product_delivery_join(0.25M).json', 'w') as f:
    json.dump(carts, f, indent=4)
