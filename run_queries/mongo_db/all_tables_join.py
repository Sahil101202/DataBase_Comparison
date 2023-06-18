import time
from pymongo import MongoClient
import json

mongo_client = MongoClient('mongodb://sahil:101202@localhost:27017/?authMechanism=DEFAULT')
mongo_db = mongo_client['db2_0_25M']
customers_collection = mongo_db['customers']
join_collection = mongo_db['customer_product_join']
products_collection = mongo_db['products']
delivery_join_collection = mongo_db['delivery_join']
delivery_companies_collection = mongo_db['delivery_companies']

times = []
first_time = []

pipeline = [
    {
        "$lookup": {
            "from": "customer_product_join",
            "localField": "id",
            "foreignField": "customer_id",
            "as": "cp"
        }
    },
    {
        "$unwind": "$cp"
    },
    {
        "$lookup": {
            "from": "products",
            "localField": "cp.product_id",
            "foreignField": "id",
            "as": "product"
        }
    },
    {
        "$unwind": "$product"
    },
    {
        "$lookup": {
            "from": "delivery_join",
            "localField": "id",
            "foreignField": "customer_id",
            "as": "dj"
        }
    },
    {
        "$unwind": "$dj"
    },
    {
        "$lookup": {
            "from": "delivery_companies",
            "localField": "dj.d_company_id",
            "foreignField": "id",
            "as": "dc"
        }
    },
    {
        "$unwind": "$dc"
    },
    {
        "$project": {
            "_id": 0,
            "first_name": "$first_name",
            "email": "$email",
            "phone_number": "$phone_number",
            "product_name": "$product.name",
            "brand": "$product.brand",
            "price": "$product.price",
            "delivery_company_name": "$dc.name",
            "delivery_company_phone": "$dc.phone"
        }
    }
]

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        data = customers_collection.aggregate(pipeline)
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
    file_path_first_time = '/Users/sahil/Desktop/db_project/times_from_query/mongodb/0_25/all_tables_first_time.json'
    file_path_times = '/Users/sahil/Desktop/db_project/times_from_query/mongodb/_025/all_tables_times.json'
    
    with open(file_path_first_time, 'w') as file:
        file.write(first_time_json_data)
        
    with open(file_path_times, 'w') as file:
        file.write(times_json_data)
    
finally:   
    mongo_client.close()
