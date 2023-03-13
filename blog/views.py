from django.shortcuts import render
from django.http import HttpResponse

# Create yoedur views here.
def indie(request):
    return HttpResponse('Blog')