from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    file_path = models.CharField(max_length=255, default='')

