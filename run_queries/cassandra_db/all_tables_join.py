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
        query = "SELECT * FROM customers"
        customer_rows = cassandra_session.execute(query)

        for customer_row in customer_rows:
            customer_id = customer_row.id

            first_name = customer_row.first_name
            email = customer_row.email
            phone_number = customer_row.phone_number

            query = "SELECT * FROM customer_product_join WHERE customer_id = %s"
            product_rows = cassandra_session.execute(query, [customer_id])

            for product_row in product_rows:
                product_id = product_row.product_id

                query = "SELECT * FROM products WHERE id = %s"
                product_result = cassandra_session.execute(query, [product_id]).one()

                if product_result:
                    product_name = product_result.name
                    product_brand = product_result.brand
                    product_price = product_result.price

                    query = "SELECT * FROM delivery_join WHERE customer_id = %s"
                    delivery_rows = cassandra_session.execute(query, [customer_id])

                    for delivery_row in delivery_rows:
                        company_id = delivery_row.d_company_id

                        query = "SELECT * FROM delivery_companies WHERE id = %s"
                        company_result = cassandra_session.execute(query, [company_id]).one()

                        if company_result:
                            company_name = company_result.name
                            company_phone = company_result.phone

                            # print(f"First Name: {first_name}")
                            # print(f"Email: {email}")
                            # print(f"Phone Number: {phone_number}")
                            # print(f"Product Name: {product_name}")
                            # print(f"Product Brand: {product_brand}")
                            # print(f"Product Price: {product_price}")
                            # print(f"Delivery Company Name: {company_name}")
                            # print(f"Delivery Company Phone: {company_phone}")
                    
        taken_time = time.time() - start_time
        if i == 0:
            first_time.append(taken_time)
        else:
            times.append(taken_time)
         
    print(first_time)   
    print(times)
    
    times_json_data = json.dumps(times)
    first_time_json_data = json.dumps(first_time)
    file_path_first_time = '/Users/sahil/Desktop/db_project/times_from_query/cassandra/0_25/all_tables_first_time.json'
    file_path_times = '/Users/sahil/Desktop/db_project/times_from_query/cassandra/_025/all_tables_times.json'
    
    with open(file_path_first_time, 'w') as file:
        file.write(first_time_json_data)
        
    with open(file_path_times, 'w') as file:
        file.write(times_json_data)
    
finally:   
    cassandra_session.shutdown()
