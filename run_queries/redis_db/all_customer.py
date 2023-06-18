import redis
import time
import json

# Connect to Redis
client = redis.Redis(host='localhost', port=6382)

times = []
first_time = []

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        data = client.hgetall('customers')
        taken_time = time.time() - start_time
        if i == 0:
            first_time.append(taken_time)
        else:
            times.append(taken_time)
         
    print(first_time)   
    print(times)
    
    times_json_data = json.dumps(times)
    first_time_json_data = json.dumps(first_time)
    file_path_first_time = 'all_customers_first_time.json'
    file_path_times = 'all_customers_times.json'
    
    with open(file_path_first_time, 'w') as file:
        file.write(first_time_json_data)
        
    with open(file_path_times, 'w') as file:
        file.write(times_json_data)
    
finally:   
    client.close()
