PROBLEM ADDRESSED

    The problem addressed in this project is to determine the most suitable DBMS for managing a big data with complex relationships and the need for high-performance querying.
    The DBMS solu<ons considered for the comparison are MySQL, MongoDB, Cassandra, Neo4j, and Redis.

DESIGN

    DEFINING DATABSES
            
        In this project we started with containers. That’s mean, first we made container for all the databases using Docker application.
        In Docker we have mysql:latest, mongo:latest, Cassandra:latest, neo4j:latest and redis:latest images to make container for MySQL, MongoDB, Cassandra, Neo4j and Redis databases respectively. ( In the project file is mentioned in docker-compose file : /docker-compose)
        Afterward, we have to make fake data to check all the functionalities of different databases. That’s the reason, we created datasets.

    MAKING FAKE DATA

        we made fake data of customer table, product table, and delivery company table. We used faker library to make fake data in python. ( file : /fake_data_scripts/fake_d.py )

        After creating different tables, we combined or join customer table and product table to have relation between them. ( file : /fake_data_scripts/cust_prod_join.py ) and we also combined that join table ( of customer and product ) with delivery_cmpanies also to have join between customer and delivery company. ( File : /fake_data_scripts/cp_join_delivery.py )

        We saved all fake data as a json object in json file and is located in datasets directory.( : /datasets )
        We made all this data for 4 different datasets.
        1. 250kcustomers(files:datasets/dataset(250000)) 
        2. 500kcustomers(files:datasets/dataset(500000)) 
        3. 750kcustomers(files:datasets/dataset(750000)) 
        4. 1Mcustomers(files:datasets/dataset(1000000))

        There is only number of customers is changing in every dataset, but number of product and delivery companies are same. That’s mean there is also different number of joins in all datasets.
        In order to visualize the performance of faker library of python, we extracted the time to make a dataset of different sizes.
        Here is the comparison of timing to make different size of dataset.

        image locatiton : images/fake_data_production.png
 

IMPLEMENTATION

    DATA ENTRY

        MYSQL : there is python script created to store all data in MySQL database. We have 5 different scripts to store data in database for data of customers, data of products and data of delivery companies. Rest of two are to join the table and make relationship between customers, products and delivery companies.
        Files: /data_saving/mysql_data

        MONGODB: for MongoDB we don’t have any python script to store data because mongo is also working on Bson objects, and it is giving feature of interface known as mongo compass. So, we can directly store data from mongo compass.

        CASSANDRA, NEO4J AND REDIS: we created scripts to store data in Cassandra, Neo4j and Redis same as MySQL database.
        Files: /data_saving/cassandra_data (for Cassandra)
        /data_saving/neo4j_data (for Neo4j) /data_saving/redis_data (for Redis)


    QUERIES
            
        We made 4 types of queries to check different functionalities or to have a proper comparison of all the databases. Below we explained those 4 queries,

        1. First query is to get all the customers like in smallest dataset, we are getting 250000 customers and in the biggest dataset, we are getting 1M customers.
        For example: MySQL
        MySQL : (file: /run_queries/mysql_db/all_customers.py)
        MongoDB : (file: /run_queries/mongo_db/all_customers.py) Cassandra : (file: /run_queries/cassandra_db/all_customers.py) Neo4j : (file: /run_queries/neo4j_db/all_customers.py)
        Redis : (file: /run_queries/redis_db/all_customers.py)

        2. Secondqueryistogetallthecustomerswhosenameisstartingfrom‘A’. For example: MySQL
        MySQL : (file: /run_queries/mysql_db/customer_with_name.py) MongoDB : (file: /run_queries/mongo_db/ customer_with_name.py) Cassandra : (file: /run_queries/cassandra_db/
        customer_with_name.py)
        Neo4j : (file: /run_queries/neo4j_db/ customer_with_name.py) Redis : (file: /run_queries/redis_db/ customer_with_name.py)

        3. Thethirdoneistojoincustomersandproducts.
        For example: MySQL
        MySQL : (file: /run_queries/mysql_db/customer_products.py) MongoDB : (file: /run_queries/mongo_db/ customer_products.py) Cassandra : (file: /run_queries/cassandra_db/ customer_products.py) Neo4j : (file: /run_queries/neo4j_db/ customer_products.py)
        Redis : (file: /run_queries/redis_db/ customer_products.py)

        4. Thelastoneistojoincustomers,products,anddeliverycompany. For example: MySQL
        MySQL : (file: /run_queries/mysql_db/all_table_join.py) MongoDB : (file: /run_queries/mongo_db/ all_table_join.py) Cassandra : (file: /run_queries/cassandra_db/ all_table_join.py) Neo4j : (file: /run_queries/neo4j_db/ all_table_join.py)
        Redis : (file: /run_queries/redis_db/ all_table_join.py)


EXPEREMENTS

            We inserted all the data in the databases. As per we know, there is four datasets, with different sizes. for example, we created 4 databases in MySQL to put 4 different sizes of datasets. And we followed same procedure to all other remaining databases (MongoDB, Cassandra, Neo4j, Redis).

    STORING DATA

        For MySQL, MongoDB, Cassandra, Neo4j and Redis we put all the data for 3 main tables (customers, products, delivery_companies) and also, we made a script to make relationship (join) in all databases. But for Neo4j and Redis, we were just able to put 3 main tables. (customers, products, and delivery_companies).

        Because to make relationship between these 2 databases (Neo4j, Redis ) it’s requiring too much time to make relationships. (only for join between customers and products for dataset of 250000 customers taking about 1 entire day ). Due to deadline, we were not able to do the relationship for Neo4j and Redis.

    TESTING QUERIES

        Since we made 4 different queries to execute in all the 5 databases with each size mentioned above. The first two queries have functionality to get data only from the customer table and last two queries are join quires.
        We wrote a script to run those four quires in all databases. But, in Neo4j and Redis we were not able to make the relationship (due to time).

        For MongoDB and Cassandra, we tried to get result of join queries and they have same problem as making relationship in the Neo4j and Redis (taking around one day or giving error like timeout).

        And for MySQL we were able to run all 4 different queries for all different size of datasets. Running those queries for 31 times we were able to take running time for all the queries every single time, then we put time_data to run first time and rest of 30 times in different Jason files. Because first time is making connection with database, and it takes more time to rest of 30.

        At the last we stored all that data in Jason files:
        For MySQL: ( /times_from_query/mysql/..) MongoDB: ( /times_from_query/mongodb/..) Cassandra: ( /times_from_query/cassandra/..) Neo4j: ( /times_from_query/neo4j/..)
        Redis: ( /times_from_query/redis/..)


ANALYSIS OF THE EXPEREMENTS

        As per we said that we extracted time to execute query first time. Here is the comparison to run first query ( to get all the customers ) with 4 different sizes of datasets. ( 250k, 500k, 750k and 1M )

    image location : images/connection_time.png
    
        We also measured the time to run query rest of 30 times to get all the customers with 4 different datasets. In the image, you can see the average of time intervals in all 5 different DBMS with 4 different datasets but, we compared MySQL and Neo4j in one graph and in another graph, we compared MongoDB, Cassandra and Redis. Because MySQL and Neo4j is taking too much time than rest of 3 DBMSs. So, if we put all in one graph then, only MySQL and Neo4j will be visible.

        Here, first we put comparison of MySQL and Neo4j. in second image, we have comparison of MongoDB, Cassandra and Redis.

    image location : images/all_customers_mysql_neo4j.png

    image location : images/all_customers_mongodb_cassandra_redis.png
 
        Then, we compared all 5 DBMSs for the second query which is to get customers whose name is starting from alphabet ‘A’.

        In the first image, you can see comparison between MySQL, Cassandra and Neo4j and in second image you can see comparison between MongoDB and Redis. The reason behind this separation is that MongoDB and Redis have very small-time intervals respect to other 3 DBMSs. So, in this way you are able to visualize histogram of all DBMSs.

    image location : images/name_with_A_mysql_neo4j_cassandra.png
 
    image location : images/name_with_A_mongodb_redis.png

COMPARISON BETWEEN ALL THE QUERIES IN MYSQL

        Since, we were able to execute all the 4 different queries in MySQL, we compared all the queries for all 4 different sized datasets, and we got some result which is showed below.

    image location : images/mysql_queries.png