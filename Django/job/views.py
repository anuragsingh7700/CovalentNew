from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Ideally - dashboard of available jobs")

def add_project(request):
    return HttpResponse("add_project ka form")
