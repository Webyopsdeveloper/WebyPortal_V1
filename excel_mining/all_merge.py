import pandas as pd
import os
import openpyxl

def inner_merge(excel_file1, sheet_name1, excel_file2, sheet_name2,common_column,output_excel_file,output_sheet_name):
    df1 = pd.read_excel(excel_file1, sheet_name=sheet_name1)
    df2 = pd.read_excel(excel_file2, sheet_name=sheet_name2)     
    merged_df = pd.merge(df1, df2, on=common_column, how="inner")
    merged_df.to_excel(output_excel_file, sheet_name=output_sheet_name, index=False)



def outer_merge(excel_file1, sheet_name1, excel_file2, sheet_name2,common_column,output_excel_file,output_sheet_name):
    df1 = pd.read_excel(excel_file1, sheet_name=sheet_name1)
    df2 = pd.read_excel(excel_file2, sheet_name=sheet_name2)     
    merged_df = pd.merge(df1, df2, on=common_column, how="outer")
    merged_df.to_excel(output_excel_file, sheet_name=output_sheet_name, index=False)



def intersection(excel_file1,sheet_name1,sheet_name2,output_excel_file,output_sheet_name):
    df1 = pd.read_excel(excel_file1, sheet_name=sheet_name1)
    df2 = pd.read_excel(excel_file2, sheet_name=sheet_name2)
    common_columns = ["First Name", "Country"]  
    intersection_df = pd.merge(df1, df2, on=common_columns)
    intersection_df.to_excel(output_excel_file, sheet_name=output_sheet_name, index=False)
    print("Intersection completed and saved to", output_excel_file)

excel_file1 = "sample_sheets/sheet3.xlsx"  
sheet_name1 = "sheet3" 
excel_file2 = "sample_sheets/sheet2.xlsx"  
sheet_name2 = "sheet2" 
common_column = "First Name" 
output_excel_file = "results/result_intersection.xlsx" 
output_sheet_name = "mergedSheet"  



inner_merge(excel_file1, sheet_name1, excel_file2, sheet_name2,common_column,output_excel_file,output_sheet_name)


# import pandas as pd

def intersection(excel_file1, sheet_name1, excel_file2, sheet_name2, output_csv_file):
    
    df1 = pd.read_excel(excel_file1, sheet_name=sheet_name1)
    df2 = pd.read_excel(excel_file2, sheet_name=sheet_name2)
    
    
    common_columns = ["First Name", "Country"]
    
    
    intersection_df = pd.merge(df1, df2, on=common_columns)
    
    
    date_columns = ["Date"]  
    for col in date_columns:
        intersection_df[col] = intersection_df[col].dt.strftime('%Y-%m-%d')  
    
    
    intersection_df.to_csv(output_csv_file, index=False)
    
    print("Intersection completed and saved to", output_csv_file)


excel_file1 = "sample_sheets/sheet3.xlsx"
sheet_name1 = "sheet3"
excel_file2 = "sample_sheets/sheet2.xlsx"
sheet_name2 = "sheet2"


output_csv_file = "results/result_intersection.csv"


intersection(excel_file1, sheet_name1, excel_file2, sheet_name2, output_csv_file)