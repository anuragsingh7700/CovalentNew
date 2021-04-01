from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import job_post


class ProjectAPI(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = job_post.objects.all()
    #def get(self):

        #project_titles = [job_post.project_name in job_post.objects.all()]
        #return Response(project_titles)


# Create your views here.
#
# def index(request):
#     return HttpResponse("Ideally - dashboard of available jobs")
#
# def add_project(request):
#     return HttpResponse("add_project ka form")
