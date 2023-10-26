from django.contrib import admin

# Register your models here.
from .models import ExcelData, Services, Candidate_Training, Documents, ScheduleMeeting, PersonalData,ApplicantDetails, contactUsForm
admin.site.register(ExcelData)
admin.site.register(Services)
admin.site.register(Candidate_Training)
admin.site.register(Documents)
admin.site.register(ScheduleMeeting)
admin.site.register(PersonalData)
admin.site.register(ApplicantDetails)
admin.site.register(contactUsForm)



