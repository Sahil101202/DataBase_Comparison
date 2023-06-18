import time
from neo4j import GraphDatabase
import json


neo4j_driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 10122002))
neo4j_session = neo4j_driver.session()

times = []
first_time = []

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        data = neo4j_session.run("MATCH (c:Customer)-[:PURCHASED]->(p:Product) MATCH (c)-[:BELONGS_TO]->(dc:DeliveryCompany) RETURN c.first_name, c.email, c.phone_number, p.name, p.brand, p.price, dc.name, dc.phone ")
        taken_time = time.time() - start_time
        if i == 0:
            first_time.append(taken_time)
        else:
            times.append(taken_time)
         
    print(first_time)   
    print(times)
    
    times_json_data = json.dumps(times)
    first_time_json_data = json.dumps(first_time)
    file_path_first_time = '/Users/sahil/Desktop/db_project/times_from_query/neo4j/0_25/all_tables_first_time.json'
    file_path_times = '/Users/sahil/Desktop/db_project/times_from_query/neo4j/_025/all_tables_times.json'
    
    with open(file_path_first_time, 'w') as file:
        file.write(first_time_json_data)
        
    with open(file_path_times, 'w') as file:
        file.write(times_json_data)
    
finally:   
    neo4j_session.close()
