import unittest
import os
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import psycopg2
from etl_final import (
    extract_from_csv, extract_from_json, extract_from_xml, extract, transform,
    load, rename_column, load_to_postgres
)

class TestScript(unittest.TestCase):

    def setUp(self):
        
        self.test_dir = "test_files"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
    
        for file_name in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file_name)
            os.remove(file_path)

        
        os.rmdir(self.test_dir)


    def test_extract_from_csv_valid_file(self):
        
        csv_data = "car_model,year_of_manufacture,price,fuel\nHonda,2020,25000,Gasoline"
        csv_file = os.path.join(self.test_dir, "test.csv")
        with open(csv_file, "w") as f:
            f.write(csv_data)

        
        dataframe = extract_from_csv(csv_file)
        self.assertIsInstance(dataframe, pd.DataFrame) 
        self.assertFalse(dataframe.empty)

    def test_extract_from_csv_invalid_file(self):
        
        csv_file = "nonexistent.csv"
        with self.assertRaises(FileNotFoundError):
            extract_from_csv(csv_file)

    

    def test_transform_rounding(self):
        
        data = {'car_model': ['Honda', 'Toyota', 'Ford'],
                'year_of_manufacture': [2020, 2019, 2022],
                'price': [25000.666, 30000.999, 15000.123],
                'fuel': ['Gasoline', 'Diesel', 'Electric']}
        df = pd.DataFrame(data)

        
        transformed_df = transform(df)

        
        expected_prices = [25000.67, 30001.00, 15000.12]
        for expected, actual in zip(expected_prices, transformed_df['price']):
            self.assertAlmostEqual(expected, actual, places=2)

    def load_to_postgres(targetfile):
        conn = psycopg2.connect(database="etl",
                                user='postgres', password='postgres',
                                host='127.0.0.1', port='5432')

        cursor = conn.cursor()
        
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS car_price (
                sr_no VARCHAR(5),
                car_model VARCHAR(100),  -- Increase the column size to accommodate longer values
                year_of_manufacture VARCHAR(200),
                price VARCHAR(50),
                fuel VARCHAR(50)
            )
        '''
        cursor.execute(create_table_query)

        
        with open(targetfile, 'r') as file:
            cursor.copy_from(file, 'car_price', sep=',', columns=('sr_no','car_model', 'year_of_manufacture', 'price', 'fuel'))

        
        select_query = "SELECT * FROM car_price"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        conn.commit()
        conn.close()
    
    def test_extract_from_json_valid_file(self):
        
        json_data = '{"car_model": "Honda", "year_of_manufacture": 2020, "price": 25000.0, "fuel": "Gasoline"}'
        json_file = os.path.join(self.test_dir, "test.json")
        with open(json_file, "w") as f:
            f.write(json_data)
        
        
        dataframe = extract_from_json(json_file)
        self.assertIsInstance(dataframe, pd.DataFrame)
        self.assertFalse(dataframe.empty)
        self.assertEqual(dataframe.iloc[0]["car_model"], "Honda")
        self.assertEqual(dataframe.iloc[0]["year_of_manufacture"], 2020)
        self.assertEqual(dataframe.iloc[0]["price"], 25000.0)
        self.assertEqual(dataframe.iloc[0]["fuel"], "Gasoline")
    
    def test_extract_from_json_invalid_file(self):
        
        json_file = "nonexistent.json"
        with self.assertRaises(FileNotFoundError):
            extract_from_json(json_file)
    
    def test_extract_from_xml_valid_file(self):
        
        xml_data = '''
            <people>
                <person>
                    <car_model>Honda</car_model>
                    <year_of_manufacture>2020</year_of_manufacture>
                    <price>25000.0</price>
                    <fuel>Gasoline</fuel>
                </person>
            </people>
        '''
        xml_file = os.path.join(self.test_dir, "test.xml")
        with open(xml_file, "w") as f:
            f.write(xml_data)
        
        
        dataframe = extract_from_xml(xml_file)
        self.assertIsInstance(dataframe, pd.DataFrame)
        self.assertFalse(dataframe.empty)
        self.assertEqual(dataframe.iloc[0]["car_model"], "Honda")
        self.assertEqual(dataframe.iloc[0]["year_of_manufacture"], 2020)
        self.assertEqual(dataframe.iloc[0]["price"], 25000.0)
        self.assertEqual(dataframe.iloc[0]["fuel"], "Gasoline")
    
    def test_extract_from_xml_invalid_file(self):
        
        xml_file = "nonexistent.xml"
        with self.assertRaises(FileNotFoundError):
            extract_from_xml(xml_file)



if __name__ == "__main__":
    unittest.main()
