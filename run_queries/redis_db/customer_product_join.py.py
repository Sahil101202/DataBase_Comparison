import redis
import time
import json

# Connect to Redis
client = redis.Redis(host='localhost', port=6379)

times = []
first_time = []

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        data = client.hgetall('cp_join')
        for join in data:
            customer_id = join['customer_id']
            product_id = join['product_id']
            customer_data = client.hgetall(f'customer: {customer_id}')
            product_data = client.hgetall(f'product: {product_id}')
            for customer in customer_data:
                for product in product_data:
                    pass
        
        taken_time = time.time() - start_time
        if i == 0:
            first_time.append(taken_time)
        else:
            times.append(taken_time)
         
    print(first_time)   
    print(times)
    
    
    times_json_data = json.dumps(times)
    first_time_json_data = json.dumps(first_time)
    file_path_first_time = '/Users/sahil/Desktop/db_project/times_from_query/redis/0_25/cp_join_first_time.json'
    file_path_times = '/Users/sahil/Desktop/db_project/times_from_query/redis/_025/cp_join_times.json'
    
    with open(file_path_first_time, 'w') as file:
        file.write(first_time_json_data)
        
    with open(file_path_times, 'w') as file:
        file.write(times_json_data)
        
finally:   
    client.close()
