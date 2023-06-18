from cassandra.cluster import Cluster
import json

# Cassandra connection details
contact_points = ['localhost']  
keyspace = 'db2_0_25M'  
table_name = 'customers'  

# Path to the JSON file
json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(250000)/customers(0.25M).json'

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
            column3_value = row['last_name']
            column4_value = row['email']
            column5_value = row['phone_number']
            column6_value = row['address']
            column7_value = row['city']
        
            # Prepare the INSERT statement
            insert_query = f"INSERT INTO {table_name} (id, name, brand, price, quantity) VALUES ({column1_value}, '{column2_value}', '{column3_value}', '{column4_value}', '{column5_value}', '{column6_value}', '{column7_value}')"

            # Execute the INSERT statements
            session.execute(insert_query)

        print("Data imported successfully!")

finally:
    # Close the session and cluster connection
    session.shutdown()
    cluster.shutdown()
