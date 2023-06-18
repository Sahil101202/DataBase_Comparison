import json
from neo4j import GraphDatabase

json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(250000)/customer_product_join(0.25M).json'

neo4j_driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', '10122002'))
neo4j_session = neo4j_driver.session()

try:
    with open(json_file) as file:
            data = json.load(file)
            
            for company in data:
                id = company['id']
                products = company["products"]
                
                for product in products:
                    pro_id = product['id']
                    data = {'c_id': id, 'p_id': pro_id}
                    
                    query = "MATCH (c:Customer {id:$c_id}) MATCH (p:Product {id:$p_id}) MERGE (c)-[:bought]->(p)"
                    
                    neo4j_session.run(query, **data)
            print("data merged successfully")
finally:
    neo4j_session.close()
    neo4j_driver.close()
    
    


