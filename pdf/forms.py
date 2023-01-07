from django import forms


#create forms
class PdfReaderForm(forms.Form):
    read_pdf = forms.FileField(widget=forms.ClearableFileInput())

