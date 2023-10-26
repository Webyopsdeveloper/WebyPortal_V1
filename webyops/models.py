from django.db import models

# Create your models here.


class ExcelData(models.Model):
    job = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=20)

class Services(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    company = models.TextField(max_length=200)

 
class Candidate_Training(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    status = models.CharField(max_length=20)
    comment = models.TextField()

class Documents(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

class ScheduleMeeting(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    contact = models.CharField(max_length=20, null=True)



class PersonalData(models.Model):
    title = models.CharField(max_length=100)
    template_view = models.CharField(max_length=100)
    action_type = models.CharField(max_length=15)
    pdf_content = models.TextField()
    def __str__(self):
        return self.title


class ApplicantDetails(models.Model):
    _JobId = models.CharField(max_length=255)
    _JobRole = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    resume_csv = models.TextField()

class contactUsForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    looking_for = models.CharField(max_length=100)
    message = models.TextField()
    

class todolist(models.Model):
    task = models.CharField(max_length=500)
    taskdetails = models.CharField(max_length=500)
    checkmark = models.CharField(max_length=20)
    comments = models.TextField()
    completed_on = models.CharField(max_length=20)

class vendorFollowUp(models.Model):
    vendor_name = models.CharField(max_length=500)
    vendor_type = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=500)
    positionToApply = models.CharField(max_length=500)
    referring_candidate = models.TextField()

class marketingCandidate(models.Model):
    candidate_name = models.CharField(max_length=500)
    personal_data = models.CharField(max_length=500)
    resume = models.CharField(max_length=500)
    email = models.CharField(max_length=20)
    comment = models.CharField(max_length=500)

class scheduleMeetingRecrt(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)

class recrtDocumentation(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

class candidateSearch(models.Model):
    candidate_name = models.CharField(max_length=500)
    visa_status = models.CharField(max_length=500)
    gender = models.CharField(max_length=100)
    technology = models.CharField(max_length=500)
    
    
    

