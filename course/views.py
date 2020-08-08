from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse('<h1>course.html</h1>')

def learn_python(request):
    return HttpResponse('<h1>coursetwo.html</H1>')