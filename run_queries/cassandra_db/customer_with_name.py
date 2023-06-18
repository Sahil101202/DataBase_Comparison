import time
from cassandra.cluster import Cluster
import json

cluster = Cluster(["127.0.0.1"])
cassandra_session = cluster.connect()
cassandra_session.set_keyspace('db2_0_1M')

times = []
first_time = []

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        data = cassandra_session.execute("SELECT * FROM customers WHERE first_name= 'Anna' ALLOW FILTERING")
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
    cassandra_session.shutdown() 
