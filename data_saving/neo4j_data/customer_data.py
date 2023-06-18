import json
from neo4j import GraphDatabase

json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(250000)/customers(0.25M).json'

neo4j_driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', '10122002'))
neo4j_session = neo4j_driver.session()

try:
    with open(json_file) as file:
            data = json.load(file)
            
            for customer in data:
                id = customer['id']
                first_name = customer['first_name']
                last_name = customer['last_name']
                email = customer['email']
                phone = customer['phone_number']
                address = customer['address']
                city = customer['city']
                
                data = {'id': id, 'first_name': first_name,'last_name': last_name, 'email': email, 'phone': phone, 'address': address, 'city': city}
                
                query = "CREATE (c:Customer {id: $id, first_name: $first_name,last_name: $last_name, email: $email, phone: $phone, address: $address, city: $city})"
                
                neo4j_session.run(query, **data)
                
            print("data inserted successfully")
finally:
    neo4j_session.close()
    neo4j_driver.close()
    
    
  


