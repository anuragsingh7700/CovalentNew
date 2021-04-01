from django.urls import path,include
from rest_framework.routers import DefaultRouter  
from . import views
from .views import StartupAPI

router = DefaultRouter()
router.register('startup',StartupAPI,basename='startup')
urlpatterns = [
    path('auth/', include(router.urls))
]