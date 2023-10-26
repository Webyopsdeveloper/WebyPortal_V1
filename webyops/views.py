from django.shortcuts import render
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ExcelData, Services, Candidate_Training, Documents, ScheduleMeeting,PersonalData,ApplicantDetails, contactUsForm, todolist, vendorFollowUp, marketingCandidate, scheduleMeetingRecrt, recrtDocumentation, candidateSearch
from .serializers import ExcelDataSerializer,ResumeDataSerializer, TrainingSerializer, DocumentsSerializer,ScheduleMeetingSerializer,PersonalDataSerializer, ApplicantSerializer,contactUsFormSerializer, todolistSerializer, vendorFollowUpSerializer, marketingCandidateSerializer, scheduleMeetingRecrtSerializer, recrtDocumentationSerializer, candidateSearchSerializer
from rest_framework.decorators import api_view
import os,tabula
import csv
import io
import fitz 
from rest_framework import viewsets
from PyPDF2 import PdfFileReader
import math ,pdfplumber

# explore jobs 
class ExcelDataAPIView(APIView):
    def post(self, request):
        file_path = os.path.join(os.getcwd(), 'webyops/explore_jobs.xlsx')

        if not os.path.exists(file_path):
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            excel_data = pd.read_excel(file_path)

            data_list = []
            for _, row in excel_data.iterrows():
                data = {
                    "jobName": self.handle_blank(row['Job']),
                    "location": self.handle_blank(row['location']),
                    "datePosted": self.format_date(row['date']),
                    "_JobId": self.handle_blank(row['_JobId']),
                    "_JobRole": self.handle_blank(row['_JobRole']),
                    "_PositionType": self.handle_blank(row['_PositionType']),
                    "_Location" :self.handle_blank(row['_Location']), 
                    "_JobDuties": self.handle_blank(row['_JobDuties']),
                    "_SkillsRequired": self.handle_blank(row['_SkillsRequired']),
                    "_ContactPerson": self.handle_blank(row['_ContactPerson']),
                }
                data_list.append(data)

            
            for data in data_list:
                serializer = ExcelDataSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()

            return Response(data_list, status=status.HTTP_201_CREATED)
        except pd.errors.ParserError:
            return Response({"error": "Invalid jobs data."}, status=status.HTTP_400_BAD_REQUEST)

    def format_date(self, date):
        try:
            return date.strftime("%Y-%m-%d")
        except (AttributeError, TypeError):
            return None  

    def handle_blank(self, value):
        if pd.isna(value) or (isinstance(value, str) and value.strip() == ""):
            return ""
        return value

class ApplicantAPI(APIView):
    def post(self, request):
        data = request.data

        
        if 'resume' not in data:
            return Response({'error': 'Missing resume field'}, status=status.HTTP_400_BAD_REQUEST)

        pdf_bytes = data['resume'].read()

        
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()

        
        csv_data = pd.DataFrame([line.split(',') for line in text.split('\n')])

        
        applicant_data = {
            '_JobId': data['_JobId'],
            '_JobRole': data['_JobRole'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'phone': data['phone'],
            'message': data['message'],
            'resume_csv': csv_data.to_csv(index=False),
        }
        serializer = ApplicantSerializer(data=applicant_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successful'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResumeAPIView(APIView):
    def post(self, request):
        
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        message = request.data.get("message")
        company = request.data.get("company")
        
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "message": message,
            "company":company
        }

        serializer = ResumeDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    
        response_data = {
            "message": "Details added to the database."
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class TrainingListView(APIView):
    def get(self, request):
        items = Candidate_Training.objects.all()
        serializer = TrainingSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentsView(APIView):
    def get(self, request):
        items = Documents.objects.all()
        serializer = DocumentsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ScheduleMeetingView(APIView):
    def get(self, request):
        items = ScheduleMeeting.objects.all()
        serializer = ScheduleMeetingSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScheduleMeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalDataView(APIView):
    def get(self, request):
        items = PersonalData.objects.all()
        serializer = PersonalDataSerializer(items, many=True)
        return Response(serializer.data)
    def post(self, request):
        
        title = request.data.get("title")
        template_view = request.data.get("template_view")
        action_type = request.data.get("action_type")
        pdf_content = request.data.get("pdf_content")

        
        if not pdf_content.content_type == 'application/pdf':
            return Response({"message": "upload a PDF file."}, status=status.HTTP_400_BAD_REQUEST)

    
        resume_text = self.extract_text_from_pdf(pdf_content)

        
        csv_data = self.convert_to_csv(resume_text)

        
        data = {
            "title": title,
            "template_view": template_view,
            "action_type": action_type,
            "pdf_content": csv_data
        }

        serializer = PersonalDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        
        response_data = {
            "message": "Details added to the database."
            
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    def extract_text_from_pdf(self, pdf_file):
        pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
        resume_text = ''
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            resume_text += page.get_text()

        return resume_text

    def convert_to_csv(self, resume_text):
        rows = resume_text.split('\n')

        
        csv_buffer = io.StringIO()
        csv_writer = csv.writer(csv_buffer)

        for row in rows:
            csv_writer.writerow([row])

        return csv_buffer.getvalue()

class contactUsFormView(APIView):
    def post(self, request):
        
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        looking_for = request.data.get("looking_for")
        message = request.data.get("message")
        
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "message": message,
            "looking_for":looking_for
        }

        serializer = contactUsFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    
        response_data = {
            "message": "successful"
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class todolistView(APIView):
    def get(self, request):
        items = todolist.objects.all()
        serializer = todolistSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = todolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class vendorFollowUpView(APIView):
    def get(self, request):
        items = vendorFollowUp.objects.all()
        serializer = vendorFollowUpSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = vendorFollowUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class marketingCandidateView(APIView):
    def get(self, request):
        items = marketingCandidate.objects.all()
        serializer = marketingCandidateSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = marketingCandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class scheduleMeetingRecrtView(APIView):
    def get(self, request):
        items = scheduleMeetingRecrt.objects.all()
        serializer = scheduleMeetingRecrtSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = scheduleMeetingRecrtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class recrtDocumentationView(APIView):
    def get(self, request):
        items = recrtDocumentation.objects.all()
        serializer = recrtDocumentationSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = recrtDocumentationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class candidateSearchView(APIView):

    def get(self, request):
        items = candidateSearch.objects.all()
        serializer = candidateSearchSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = candidateSearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)