from cassandra.cluster import Cluster
import json

# Cassandra connection details
contact_points = ['localhost']  
keyspace = 'db2_0_1M'  
table_name = 'delivery_join'  

# Path to the JSON file
json_file = '/Users/sahil/Desktop/db_project/datasets/dataset(1000000)/customer_product_delivery_join(1M).json'

cluster = Cluster(contact_points=contact_points)
session = cluster.connect(keyspace)

try:
    # Open the JSON file
    with open(json_file) as file:
        data = json.load(file)
        
        # Extract the data from the JSON file
        for row in data:
            # Assuming the JSON data has keys corresponding to the table columns
            column1_value = row['id']
            column2_value = row['first_name']
            companies = row['delivery_company']
            
            for company in companies:
                column3_value = company['id']
                column4_value = company['name']
                # Prepare the INSERT statement
                insert_query = f"INSERT INTO {table_name} (customer_id, customer_name, d_company_id, d_company_name) VALUES ({column1_value}, '{column2_value}', {column3_value}, '{column4_value}')"

                # Execute the INSERT statements
                session.execute(insert_query)

        print("Data imported successfully!")

finally:
    # Close the session and cluster connection
    session.shutdown()
    cluster.shutdown()
