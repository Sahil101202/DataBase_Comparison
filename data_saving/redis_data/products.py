import redis
import json

# Connect to Redis
client = redis.Redis(host='localhost', port=6382)

# Path to the JSON file
json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(1000000)/products(1M).json'

try:
    # Open the JSON file
    with open(json_file) as file:
        data = json.load(file)
        
        for product in data:
            id = product['id']
            
            # Save customers using Redis Hash data structure
            client.hset('products75', id, str(product))

        print("Data imported successfully!")

finally:
    # Close the database connection
    client.close()
