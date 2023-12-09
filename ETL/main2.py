import psycopg2
# import pandas as pd

# filename = "dealership_transformed_data1.csv"

# df = pd.read_csv(filename)
# columns = df.columns.tolist()
# print(columns)  # Print the column names


conn = psycopg2.connect(database="etl",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432')

cursor = conn.cursor()


create_table_query = '''
    CREATE TABLE IF NOT EXISTS car_price (
        sr_no VARCHAR(5),
        car_model VARCHAR(200),
        year_of_manufacture VARCHAR(200),
        price VARCHAR(50),
        fuel VARCHAR(50)
        
    )
'''
cursor.execute(create_table_query)


with open('dealership_transformed_data1.csv', 'r') as file:
    cursor.copy_from(file, 'car_price', sep=',', columns=('sr_no','car_model', 'year_of_manufacture', 'price', 'fuel'))


select_query = "SELECT * FROM car_price"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
