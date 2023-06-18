import time
import pymysql
import json

host = 'localhost'
user = 'root'
password = '101202'
database = 'db2_0_1M'

connection = pymysql.connect(host=host,user=user,password=password,database=database)
cursor = connection.cursor()

times = []
first_time = []

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        data = cursor.execute("SELECT c.id, c.first_name, c.email, c.phone_number, p.name, p.brand, p.price FROM customers c JOIN customer_product_join cp ON c.id = cp.customer_id JOIN products p ON p.id=cp.product_id")
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
    file_path_first_time = 'cp_join_first_time.json'
    file_path_times = 'cp_join_times.json'
    
    with open(file_path_first_time, 'w') as file:
        file.write(first_time_json_data)
        
    with open(file_path_times, 'w') as file:
        file.write(times_json_data)
    
finally:   
    connection.close()
