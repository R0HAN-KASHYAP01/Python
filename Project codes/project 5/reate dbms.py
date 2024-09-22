import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='12345678')
cursor = conn.cursor()

database_creation_query = "CREATE DATABASE IF NOT EXISTS grocery_shop"
cursor.execute(database_creation_query)

cursor.execute("USE grocery_shop")

customer_table_creation_query = """
CREATE TABLE IF NOT EXISTS customer_details (
    phone_no INT PRIMARY KEY,
    cust_name VARCHAR(255),
    cost FLOAT
)
"""
cursor.execute(customer_table_creation_query)


product_table_creation_query = """
CREATE TABLE IF NOT EXISTS product_details (
    product_name VARCHAR(255) PRIMARY KEY,
    product_cost FLOAT
)
"""
cursor.execute(product_table_creation_query)

worker_table_creation_query = """
CREATE TABLE IF NOT EXISTS worker_details (
    worker_name VARCHAR(255),
    worker_work VARCHAR(255),
    worker_age INT,
    worker_salary FLOAT,
    phone_no INT PRIMARY KEY
)
"""
cursor.execute(worker_table_creation_query)

conn.commit()
conn.close()

