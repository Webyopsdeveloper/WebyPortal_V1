from django.db import models

# Create your models here.
from django.db import models

class UploadedFile(models.Model):
    file1 = models.FileField(upload_to='uploads/')
    file2 = models.FileField(upload_to='uploads/')
    merged_result = models.FileField(upload_to='merged_results/', null=True)




class ExcelToCsv(models.Model):
    csv_file = models.TextField()
    sheet_id = models.CharField(max_length=500)  # Add a new field for the sheet ID

    def __str__(self):
        return self.sheet_id


