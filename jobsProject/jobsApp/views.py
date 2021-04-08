from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    s = '<h1>Welcome To jobs.com</h1>'
    return HttpResponse(s)

def lhrjobsinfo(request):
    s = '<h1>Lahore jobs information</h1>'
    return HttpResponse(s)


def krachijobsinfo(request):
    s = '<h1>Krachi jobs information</h1>'
    return HttpResponse(s)


def isljobsinfo(request):
    s = '<h1>IslamAbad jobs information</h1>'
    return HttpResponse(s)