from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=file.pdf"
    p = canvas.Canvas(response)
    p.setFont('Times-Roman', 55)
    p.drawString(100, 700, 'Hello JavaPoint.')
    p.showPage()
    p.save()
    return response

def readpdf(request):
    if request.method == "POST":
        form = PdfReaderForm(request.FILES)
        if form.is_valid():
            read_pdf = request.FILES('read_pdf')
            image_date = open(read_pdf,'rb').read()
            print(image_date)
    else:
        form = PdfReaderForm()

    return render(request, 'pdf.html', {'form':form})