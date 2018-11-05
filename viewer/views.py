from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
import pandas
from .models import File
# Create your views here.


def home(request):
    return render(request, 'home.html')


def upload(request):  # FileUpload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            viewer(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
    return render(request, 'upload.html', {'File': File, 'form': form})


def reader(request):  # Reads the Uploaded CSV
    table = pandas.read_csv('file.csv')


def viewer(request):  # Renders the Uploaded CSV
    pass


def opcreator(request):  # Picks column names from table for options
    pass


def sorting(request):  # Sorting the table
    pass
