from django.db.models import fields
from rest_framework import serializers
from .models import job_post

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tags
#         fields = ['title']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_post
        fields = ['project_name', 'project_description', 'tags', 'duration', 'timestamp', 'status']
