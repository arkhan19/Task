from django import forms


class FileForm(forms.Form):
    file = forms.FileField(
        help_text='Upload only CSV file'
    )

