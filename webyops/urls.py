from django.urls import path
from .views import ExcelDataAPIView, ResumeAPIView  , TrainingListView, DocumentsView, ScheduleMeetingView, PersonalDataView, ApplicantAPI, contactUsFormView, todolistView, vendorFollowUpView, marketingCandidateView, scheduleMeetingRecrtView, recrtDocumentationView, candidateSearchView
from . import views

urlpatterns = [
    path('explore-jobs', ExcelDataAPIView.as_view(), name='excel_data'),
    path('applicant-details', ApplicantAPI.as_view(), name='applicant-api'),
    path('services', ResumeAPIView.as_view(), name='resume_api'),
    path('candidateTraining',TrainingListView.as_view(),name = 'training-list' ),
    path('documents',DocumentsView.as_view(),name = 'documents'),
    path('scheduleMeeting',ScheduleMeetingView.as_view(),name = 'schedule-meeting'),
    path('personal-data', PersonalDataView.as_view(), name='personal-data'),
    path('contact-us', contactUsFormView.as_view(), name='contact-us'),
    path('todolist', todolistView.as_view(), name='todo-list'),
    path('vendor', vendorFollowUpView.as_view(), name='vendor'),
    path('marketingCandidate', marketingCandidateView.as_view(), name='marketing-candidate'),
    path('scheduleMeetingRecrt', scheduleMeetingRecrtView.as_view(), name='scheduleMeeting-recrtuiter'),
    path('recrtDocumentation', recrtDocumentationView.as_view(), name='recrtuiter-documents'),
    path('candidateSearch', candidateSearchView.as_view(), name='candidateSearch'),

]


