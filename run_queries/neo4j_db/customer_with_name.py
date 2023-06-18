import time
from neo4j import GraphDatabase
import json

neo4j_driver = GraphDatabase.driver('bolt://localhost:7690', auth=('neo4j', str(10122002)))
neo4j_session = neo4j_driver.session()

times = []
first_time = []

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        data = neo4j_session.run("MATCH (c:Customer) WHERE c.first_name STARTS WITH 'A' RETURN c")
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
    neo4j_session.close()
