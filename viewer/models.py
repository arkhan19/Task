from django.db import models
import os
# Create your models here.
from Task import settings


class File(models.Model):
    name = models.CharField(max_length=255, blank=True)
    file_field = models.FileField(upload_to='files/%Y/%m/%d')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.file_field.name

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file_field.name))

