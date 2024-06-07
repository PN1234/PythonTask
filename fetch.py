import getdata
import psycopg2


try:
    hostname = 'localhost'
    database = 'DataAPI'
    username = 'postgres'
    pwd = '123456'
    port_id = '5432'
    
    con = psycopg2.connect(
    host = hostname,
    database = database,
    user = username,
    password = pwd,
    port = port_id
)

    curr = con.cursor()
    
    create_countries_table = """CREATE TABLE IF NOT EXISTS country(
      id VARCHAR(10) PRIMARY KEY,
      name VARCHAR(255) UNIQUE NOT NULL,
      iso3code VARCHAR(255) UNIQUE NOT NULL     
    )"""

    curr.execute(create_countries_table)
    con.commit()

    create_gdp_table = """CREATE TABLE IF NOT EXISTS GDP(
        country_id VARCHAR(10),
        YEAR INTEGER NOT NULL,
        value DOUBLE PRECISION,
        FOREIGN KEY(country_id) REFERENCES country(id)
       );
       """
    curr.execute(create_gdp_table)
    con.commit()    
    new_data = [(countries['country']['id'] , countries['country']['value'],countries["countryiso3code"]) for countries in getdata.newapidata]
    # print(new_data)
    #print(len(new_data))
    insert_query = """INSERT INTO country(id,name,iso3code) VALUES(%s,%s,%s) ON CONFLICT(id) DO NOTHING"""
    curr.executemany(insert_query,new_data)   
    con.commit()
    count = 0 
    if count==0:
        new_data_gdp = [(gdpdata['country']['id'],gdpdata['date'],gdpdata['value']) for gdpdata in getdata.newapidata]
        insert_query2 = """INSERT INTO gdp(country_id,year,value) VALUES(%s,%s,%s)"""
        curr.executemany(insert_query2,new_data_gdp)
        con.commit()

except Exception as e:
    print("Exception occurred",e)

else:
    count += 1
    print("Database Connection is Successfull")  

finally:
    con.close()
    curr.close()
