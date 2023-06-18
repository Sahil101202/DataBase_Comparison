import time
from pymongo import MongoClient
import json

mongo_client = MongoClient('mongodb://sahil:101202@localhost:27017/?authMechanism=DEFAULT')
mongo_db = mongo_client['db2_0_1M']
mongo_collection = mongo_db['customers']

times = []
first_time = []

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        query = {"first_name": {"$regex": "^A"}}
        data = mongo_collection.find(query)
        print(data)
        taken_time = time.time() - start_time
        if i == 0:
            first_time.append(taken_time)
        else:
            times.append(taken_time)
         
    print(first_time)   
    print(times)
    
    times_json_data = json.dumps(times)
    first_time_json_data = json.dumps(first_time)
    file_path_first_time = 'customer_with_name_first_time.json'
    file_path_times = 'customer_with_name_times.json'
    
    with open(file_path_first_time, 'w') as file:
        file.write(first_time_json_data)
        
    with open(file_path_times, 'w') as file:
        file.write(times_json_data)
    
finally:   
    mongo_client.close()
