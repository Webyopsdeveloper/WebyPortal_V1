import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ExcelToCsv
import uuid

class InnerMergeView(APIView):
    def post(self, request):
        file1 = request.data.get('file1')
        file2 = request.data.get('file2')

        if not file1 or not file2:
            return Response({'error': 'Both files are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)

        
            merged_inner = pd.merge(df1, df2, on='First Name', how='inner')

            
            csv_inner = merged_inner.to_csv(index=False)

        
            csv_response = {
                'csv_inner': csv_inner
            }

            return Response(csv_response)

        except pd.errors.ParserError:
            return Response({'error': 'Invalid Excel file format.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OuterMergeView(APIView):
    def post(self, request):
        file1 = request.data.get('file1')
        file2 = request.data.get('file2')

        if not file1 or not file2:
            return Response({'error': 'Both files are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)

            
            merged_outer = pd.merge(df1, df2, on='First Name', how='outer')

            
            csv_outer = merged_outer.to_csv(index=False)

            
            csv_response = {
                'csv_outer': csv_outer
            }

            return Response(csv_response)

        except pd.errors.ParserError:
            return Response({'error': 'Invalid Excel file format.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class IntersectionMergeView(APIView):
    def post(self, request):
        file1 = request.data.get('file1')
        file2 = request.data.get('file2')

        if not file1 or not file2:
            return Response({'error': 'Both files are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)

            
            merged_intersection = pd.merge(df1, df2, on='First Name', how='inner')

            
            csv_intersection = merged_intersection.to_csv(index=False)

            
            csv_response = {
                'csv_intersection': csv_intersection
            }

            return Response(csv_response)

        except pd.errors.ParserError:
            return Response({'error': 'Invalid Excel file format.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CountSubSheetsView(APIView):
    def post(self, request):
        file1 = request.data.get('file1')
        file2 = request.data.get('file2')

        if not file1 or not file2:
            return Response({'error': 'Both files are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            
            xl1 = pd.ExcelFile(file1)
            xl2 = pd.ExcelFile(file2)

            num_sheets_file1 = len(xl1.sheet_names)
            num_sheets_file2 = len(xl2.sheet_names)

        
            count_response = {
                'num_sheets_file1': num_sheets_file1,
                'num_sheets_file2': num_sheets_file2
            }

            return Response(count_response)

        except pd.errors.ParserError:
            return Response({'error': 'Invalid Excel file format.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ExcelToCsvView(APIView):
    def post(self, request):
        excel_file = request.data.get('excel_file')

        if not excel_file:
            return Response({'error': 'Excel file is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            
            df = pd.read_excel(excel_file)

            
            csv_data = df.to_csv(index=False)

            # Generate a unique sheet ID using uuid
            sheet_id = str(uuid.uuid4())

            # Save CSV data to the database
            ExcelToCsv.objects.create(
                csv_file=csv_data,
                sheet_id=sheet_id
            )

            return Response({'message': 'Excel data converted to CSV and saved.', 'sheet_id': sheet_id})

        except pd.errors.ParserError:
            return Response({'error': 'Invalid Excel file format.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        