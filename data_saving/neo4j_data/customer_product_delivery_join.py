import json
from neo4j import GraphDatabase

json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(250000)/customer_product_delivery_join(0.25M).json'

neo4j_driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', '10122002'))
neo4j_session = neo4j_driver.session()

try:
    with open(json_file) as file:
            data = json.load(file)
            
            for company in data:
                id = company['id']
                companies = company["delivery_company"]
                
                for d_company in companies:
                    d_id = d_company['id']
                    data = {'c_id': id, 'c_id': d_id}
                    
                    query = "MATCH (c:Customer {id:$c_id}) MATCH (dc:DCompany {id:$d_id}) MERGE (c)-[:delivered_by]->(dc)"
                    
                    neo4j_session.run(query, **data)
            print("data merged successfully")
finally:
    neo4j_session.close()
    neo4j_driver.close()
    
    


