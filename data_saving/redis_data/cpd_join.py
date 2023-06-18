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
            company = cp_join['delivery_company']
            for i in company:
                company_id = i['id']
            
                join = {
                    'customer_id':customer_id,
                    'dcompany_id' :company_id
                }
                
                # Save customers using Redis Hash data structure
                client.hset('cpd_join100', company_id, str(join))

        print("Data imported successfully!")

finally:
    # Close the database connection
    client.close()







