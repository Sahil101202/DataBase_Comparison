import json
from neo4j import GraphDatabase

json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(250000)/products(0.25M).json'

neo4j_driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', '10122002'))
neo4j_session = neo4j_driver.session()

try:
    with open(json_file) as file:
            data = json.load(file)
            
            for product in data:
                id = product['id']
                name = product['name']
                brand = product['brand']
                price = product['price']
                quantity = product['quantity']
                
                data = {'id': id, 'name': name,'brand': brand, 'price': price, 'quantity': quantity}
                
                query = "CREATE (p:Product {id: $id, name: $name,brand: $brand, price: $price, quantity: $quantity})"
                
                neo4j_session.run(query, **data)
                
            print("data inserted successfully")
finally:
    neo4j_session.close()
    neo4j_driver.close()
    
    


