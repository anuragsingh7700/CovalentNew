from django.contrib.auth.base_user import BaseUserManager
from .roles import ADMIN



class SiteUserManager(BaseUserManager):

    def create_user(self,email,password,**extra):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra):
        extra.setdefault('is_active',True)
        extra.setdefault('role',ADMIN)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_staff',True)
        print(extra)
        if extra.get('role') != ADMIN:
            raise ValueError('Superuser permisisons are not granted')
        return self.create_user(email,password,**extra)
