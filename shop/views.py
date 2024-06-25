from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, 'index.html')


def header_view(request):
    return render(request, 'shared/Header.html')


def footer_view(request):
    return render(request, 'shared/Footer.html')

