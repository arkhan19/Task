from django import forms
from .models import File


class FileForm(forms.Form):
    file = forms.FileField(
        label='Select a file NOW',
        help_text='max. 2.5 megabytes'
    )

