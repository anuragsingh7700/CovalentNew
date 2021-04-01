from rest_framework import serializers
from .models import job_post

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_post
        fields = ['project_name', 'project_description', 'tags', 'duration', 'timestamp', 'status']
