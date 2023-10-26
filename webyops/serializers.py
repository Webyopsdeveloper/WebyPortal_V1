from rest_framework import serializers
from .models import ExcelData, Services, Candidate_Training, Documents, ScheduleMeeting,PersonalData,ApplicantDetails, contactUsForm, todolist, vendorFollowUp, marketingCandidate, scheduleMeetingRecrt, recrtDocumentation, candidateSearch

class ExcelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelData
        fields = '__all__'
class ResumeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate_Training
        fields = ['id', 'name', 'link', 'status', 'comment']
class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'
        
class ScheduleMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleMeeting
        fields = '__all__'


class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantDetails
        fields = '__all__'

class contactUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactUsForm
        fields = '__all__'
    
class todolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = todolist
        fields = '__all__'
class vendorFollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendorFollowUp
        fields = '__all__'

class marketingCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = marketingCandidate
        fields = '__all__'
class scheduleMeetingRecrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = scheduleMeetingRecrt
        fields = '__all__'
class recrtDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = recrtDocumentation
        fields = '__all__'

class candidateSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = candidateSearch
        fields = '__all__'