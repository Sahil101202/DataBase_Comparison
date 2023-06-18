import redis
import json

# Connect to Redis
client = redis.Redis(host='localhost', port=6382)

# Path to the JSON file
json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(250000)/customer_product_join(0.25M).json'

try:
    # Open the JSON file
    with open(json_file) as file:
        data = json.load(file)
        
        for cp_join in data:
            customer_id = cp_join['id']
            product = cp_join['products']
            for i in product:
                product_id = i['id']
            
                join = {
                    'customer_id':customer_id,
                    'product_id' :product_id
                }
                
                # Save customers using Redis Hash data structure
                client.hset('cp_join100', product_id, str(join))

        print("Data imported successfully!")

finally:
    # Close the database connection
    client.close()







