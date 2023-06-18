from cassandra.cluster import Cluster
import json

# Cassandra connection details
contact_points = ['localhost']  
keyspace = 'db2_0_1M'  
table_name = 'customer_product_join'  

# Path to the JSON file
json_file = '/Users/sahil/Desktop/db_project/datasets/dataset(1000000)/customer_product_join(1M).json'

cluster = Cluster(contact_points=contact_points)
session = cluster.connect(keyspace)

try:
    # Open the JSON file
    with open(json_file) as file:
        data = json.load(file)
        
        order_id = 1
        # Extract the data from the JSON file
        for row in data:
            # Assuming the JSON data has keys corresponding to the table columns
            column1_value = row['id']
            column2_value = row['first_name']
            products = row['products']
            
            for product in products:
                column3_value = product['id']
                column4_value = product['name']
                # Prepare the INSERT statement
                insert_query = f"INSERT INTO {table_name} (order_id, customer_id, customer_name, product_id, product_name) VALUES ({order_id}, {column1_value}, '{column2_value}', {column3_value}, '{column4_value}')"

                # Execute the INSERT statements
                session.execute(insert_query)
                order_id += 1

        print("Data imported successfully!")

finally:
    # Close the session and cluster connection
    session.shutdown()
    cluster.shutdown()
