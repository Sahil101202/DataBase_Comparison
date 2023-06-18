import redis
import json

# Connect to Redis
client = redis.Redis(host='localhost', port=6382)

# Path to the JSON file
json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(1000000)/delivery_companies(1M).json'

try:
    # Open the JSON file
    with open(json_file) as file:
        data = json.load(file)
        
        for company in data:
            id = company['id']
            
            # Save customers using Redis Hash data structure
            client.hset('dcompany100', id, str(company))

        print("Data imported successfully!")

finally:
    # Close the database connection
    client.close()
