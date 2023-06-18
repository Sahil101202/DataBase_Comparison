import time
from cassandra.cluster import Cluster
import json

cluster = Cluster(["127.0.0.1"])
cassandra_session = cluster.connect()
cassandra_session.set_keyspace('db2_0_25M')

times = []
first_time = []

try:
    n = 31
    for i in range(n):
        start_time = time.time()
        customer_query = "SELECT id FROM customers"
        customer_results = cassandra_session.execute(customer_query)

        for customer_row in customer_results:
            customer_id = customer_row.id
            product_query = f"SELECT product_id FROM customer_product_join WHERE customer_id = {customer_id}"
            product_results = cassandra_session.execute(product_query)

            for product_row in product_results:
                product_id = product_row.product_id
                details_query = f"SELECT name, brand, price FROM products WHERE id = {product_id}"
                details_result = cassandra_session.execute(details_query)

                for details_row in details_result:
                    pass
                    # print("Customer ID:", customer_id)
                    # print("Customer Name:", customer_row.first_name)
                    # print("Customer Email:", customer_row.email)
                    # print("Customer Phone Number:", customer_row.phone_number)
                    # print("Product Name:", details_row.name)
                    # print("Product Brand:", details_row.brand)
                    # print("Product Price:", details_row.price)
        taken_time = time.time() - start_time
        if i == 0:
            first_time.append(taken_time)
        else:
            times.append(taken_time)
         
    print(first_time)   
    print(times)
    
    times_json_data = json.dumps(times)
    first_time_json_data = json.dumps(first_time)
    file_path_first_time = '/Users/sahil/Desktop/db_project/times_from_query/cassandra/0_25/cp_join_first_time.json'
    file_path_times = '/Users/sahil/Desktop/db_project/times_from_query/cassandra/_025/cp_join_times.json'
    
    with open(file_path_first_time, 'w') as file:
        file.write(first_time_json_data)
        
    with open(file_path_times, 'w') as file:
        file.write(times_json_data)
    
finally:   
    cassandra_session.shutdown()
