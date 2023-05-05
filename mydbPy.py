import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="unicorn_user",
                                  password="magical_password",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="training")
    cursor = connection.cursor()
    #creiamo tabella
    create_table_query = '''CREATE TABLE mobile
              (ID SERIAL PRIMARY KEY     NOT NULL,
              MODEL           TEXT    NOT NULL,
              PRICE         REAL); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    #inseriamo dati
    insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
    cursor.execute(insert_query)
    connection.commit()
    #visualiziamo con SELECT
    cursor.execute("SELECT * from mobile")
    record = cursor.fetchall()
    print("Result ", record)




except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
