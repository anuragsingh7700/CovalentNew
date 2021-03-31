from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets


# Create your views here.
def index(request):
    return HttpResponse("Hello! I am a startup or I am a member page")

def register(request):
    return HttpResponse("Register page")

def login(request):
    return HttpResponse("Login page")
