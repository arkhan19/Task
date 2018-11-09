from django import forms


class FileForm(forms.Form):
    file = forms.FileField(
        help_text='max. 2.5 megabytes'
    )

