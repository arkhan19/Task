from django.db import models

# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=255, blank=True)
    file_field = models.FileField(upload_to='files/%Y/%m/%d')  # if the files are not organised change it to 'files/%Y/%m/%d'.
    uploaded = models.DateTimeField(auto_now_add=True)
