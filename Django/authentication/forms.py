from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm

from .models import Member, SiteUser, Startup




class UserForm(forms.ModelForm):
    class Meta:
        model = SiteUser

class StartupCreationForm(ModelForm):
    class Meta():
        model = Startup
        fields = ('company_name','contact_no','gstin')

class MemberCreationForm(ModelForm):
    
    class Meta():
        model = Member
        fields = ('first_name','last_name','joinig_code')