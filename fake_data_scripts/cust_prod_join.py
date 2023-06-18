import json
import random

# Load customers data from JSON file
with open('customers(0.25M).json', 'r') as f:
    customers = json.load(f)

# Load electronic products data from JSON file
with open('products(0.25M).json', 'r') as f:
    products = json.load(f)

# Randomly assign electronic products to customers
for customer in customers:
    customer['products'] = random.sample(products, random.randint(1, 5))

# Save joined data to JSON file
with open('customer_product_join(0.25M).json', 'w') as f:
    json.dump(customers, f, indent=4)
