import json
from faker import Faker
import random
import time

fake = Faker()

time_taken = {}

#### Generate fake customer data

customers = []
def generate_fake_customer():
    customer = {
        'id': fake.unique.random_number(digits=6),
        'first_name': fake.first_name(),
        'last_name':fake.last_name(),
        'email': fake.unique.email(),
        'phone_number': fake.unique.phone_number(),
        'address': fake.unique.address(),
        'city':fake.city()
    }
    return customer

start_time_customer = time.time()

for _ in range(250000):
    customer = generate_fake_customer()
    customers.append(customer)

customer_time = time.time() - start_time_customer
time_taken['customer_time_taken(0.25M)'] = str(customer_time)

#### Generate fake electronic product data

products = []
def generate_fake_electronic_product():
    product = {
        'id': fake.unique.random_number(digits=6),
        'name': fake.unique.word() + ' ' + random.choice(['Laptop', 'Phone', 'Tablet', 'earphones', 'headphones', 'TV', 'monitor']),
        'brand': fake.company(),
        'price': round(random.uniform(100, 2000), 2),
        'quantity': random.randint(1, 1000)
    }
    return product

start_time_product = time.time()
for _ in range(500):
    product = generate_fake_electronic_product()
    products.append(product)
product_time = time.time() - start_time_product
time_taken['product_time_taken(0.25M)'] = str(product_time)
    


#### Generate fake delivery company data

delivery_companies_list = ["UPS","FedEx","DHL","USPS","Amazon Logistics","Royal Mail","TNT Express","DPD","Hermes","PostNL","Canada Post","Australia Post","Purolator","Chronopost","Correos","La Poste","ParcelForce","Poste Italiane","S.F. Express","Yamato Transport","Deutsche Post","New Zealand Post","China Post","Singapore Post","Korea Post","Swiss Post","Belgium Post","Aramex","PostNord","GLS","Colissimo","Seur","Skynet","Poste Maroc","India Post","Toll Group","Japan Post","Pos Malaysia","South African Post Office","Vietnam Post","Nippon Express","An Post","Poczta Polska","Thailand Post","Poste Tunisienne","Poste Algérie","Qatar Post","Pos Indonesia","Egypt Post","Poste Libanaise","Oman Post"]

start_time_delivery = time.time()
delivery_companies = []
for i in range(len(delivery_companies_list)):
    company = {
        'id': fake.unique.random_number(digits=6),
        'name': delivery_companies_list[i],
        'phone': fake.unique.phone_number()
    }
    delivery_companies.append(company)
delivery_time = time.time() - start_time_delivery
time_taken['delivery_time_taken(0.25M)'] = str(delivery_time)


# Write data to JSON files

with open('customers(0.25M).json', 'w') as file:
    json.dump(customers, file, indent=4)
    
with open('products(0.25M).json', 'w') as file:
    json.dump(products, file, indent=4)
    
with open('delivery_companies(0.25M).json', 'w') as file:
    json.dump(delivery_companies, file, indent=4)
    
with open('time_taken(0.25M).txt', 'w') as fp:
    for times in time_taken:
        fp.write("%s : " % times)
        fp.write("%s\n" % time_taken[times])
    



