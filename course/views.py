from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    return HttpResponse('<h1>Hello django</h1>')

def learn_python(request):
    return HttpResponse('<h1>hello python</h1>')