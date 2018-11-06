import csv

from django.shortcuts import render, reverse, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template import RequestContext
# from django.views import View
from .forms import FileForm  # used by upload function
import pandas
from .models import File
# Create your views here.


def home(request):
    return render(request, 'home.html')


def upload(request):  # FileUpload
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # newfile = File(file=request.FILES['file'])
            # newfile.save()
            file = request.FILES['file']
            messages.success(request, "File Upload DONE")

            decoded_file = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                print(row)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('views.home'))
    else:
        form = FileForm()  # A empty, unbound form

            # Load documents for the list page
        files = File.objects.all()

        # Render list page with the documents and the form
        return render_to_response('upload.html', {'files':files, 'form':form})
