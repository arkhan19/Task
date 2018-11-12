import csv, json, requests
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.conf import settings
import os
from .forms import FileForm
from .models import File


def home(request):
    return render(request, 'home.html')


class View(generics.RetrieveAPIView):
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        obj = File.objects.order_by('-id')[0]
        path = os.path.join(settings.MEDIA_ROOT, obj.file_field.path)
        data = csvtojson(path)
        data = json.dumps(data)
        data = json.loads(data)
        return Response({'data': data}, template_name = 'viewer.html')


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES) # A non-empty, bound form
        if form.is_valid():
            file = File(file_field=request.FILES['file'])
            file.save()
            return HttpResponseRedirect(reverse('viewer'))
    else:
        form = FileForm()  # A empty, unbound form
    return render(request, 'upload.html', {'form': form, 'path': dir})


def csvtojson(f):
    csvfile = open(f, 'r')
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
        data.append(row)

    data = json.loads(json.dumps(data))
    return data