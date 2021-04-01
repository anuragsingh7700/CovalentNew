from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import ProjectAPI

router = DefaultRouter()
router.register('project_dashboard', ProjectAPI, basename='project')
urlpatterns = [
    path('projects/', include(router.urls))
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('add_new', views.add_project, name='Add New'),
# ]