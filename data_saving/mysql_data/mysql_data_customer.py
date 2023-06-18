import json
import pymysql

# MySQL database connection details
host = 'localhost'
user = 'root'
password = '101202'
database = 'db2_0_1M'

password = password.encode('utf-8')

# Path to the JSON file
json_file = '/Users/sahil/Desktop/db_project/datasets/dataset(1000000)/customers(1M).json'

# Table name in phpMyAdmin to save the data
table_name = 'customers'

# Connect to the MySQL database
connection = pymysql.connect(host=host,user=user,password=password,database=database)

try:
    # Open the JSON file
    with open(json_file) as file:
        data = json.load(file)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Iterate through the rows and insert them into the table
        for row in data:
            # Assuming the JSON data has keys corresponding to the table columns
            column1_value = row['id']
            column2_value = row['first_name']
            column3_value = row['last_name']
            column4_value = row['email']
            column5_value = row['phone_number']
            column6_value = row['address']
            column7_value = row['city']
            # Add more columns as needed

            # SQL query to insert data into the table
            sql = f"INSERT INTO {table_name} (id, first_name, last_name, email, phone_number, address, city) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            # Modify the above query to include more columns

            # Execute the query with the data
            cursor.execute(sql, (column1_value, column2_value, column3_value, column4_value, column5_value, column6_value, column7_value))
            # Modify the above line to include more column values

        # Commit the changes to the database
        connection.commit()

        print("Data imported successfully!")

finally:
    # Close the database connection
    connection.close()
