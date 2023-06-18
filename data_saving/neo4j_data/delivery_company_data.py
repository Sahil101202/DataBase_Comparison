import json
from neo4j import GraphDatabase

json_file = '/Users/sahil/Desktop/db_project/datasets/datasets(250000)/delivery_companies(0.25M).json'

neo4j_driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', '10122002'))
neo4j_session = neo4j_driver.session()


try:
    with open(json_file) as file:
            data = json.load(file)
            
            for company in data:
                id = company['id']
                name = company['name']
                phone = company['phone']
                
                data = {'id': id, 'name': name,'phone': phone}
                
                query = "CREATE (dc:DCompany {id: $id, name: $name, phone: $phone})"
                
                neo4j_session.run(query, **data)
                
            print("data inserted successfully")
finally:
    neo4j_session.close()
    neo4j_driver.close()
    
    


