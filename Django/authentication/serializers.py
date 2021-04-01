from rest_framework import serializers
from .models import Startup

class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ['registration_no','company_name','contact_no','company_email','date_of_creation','industry','sector','company_code']
