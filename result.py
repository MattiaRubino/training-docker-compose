import psycopg2
from psycopg2 import Error
f = None

try:
  f = open("cities.csv")
  lines =f.read().splitlines()
  lines=lines[1:len(lines)-2]
  elements=[]
  i=1
  for line in lines:
     dato=line.split(",")
     cities=(i,dato[0], dato[1],dato[2],dato[3], dato[4], dato[5],dato[6],dato[7],dato[8],dato[9])
     elements.append(cities)
     i+=1

except Exception as e:
        print(e)
finally:
    if f is not None:
       f.close()

try:
    connection = psycopg2.connect(user="unicorn_user",
                                  password="magical_password",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="training")

    cursor = connection.cursor()
    insert_query = "INSERT INTO città (ID ,LatD, LatM,LatS,NS,LonD,LonM,LonS,EW,City,State)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(insert_query, elements)
    db.commit()
    cursor.execute("SELECT * from città")
    record = cursor.fetchall()
    print("Result ", record)


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
