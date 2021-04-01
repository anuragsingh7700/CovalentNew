from rest_framework import viewsets
from .serializers import StartupSerializer
from .models import Startup

class StartupAPI(viewsets.ModelViewSet):
    serializer_class = StartupSerializer
    queryset = Startup.objects.all()
    # permission_classes = [IsAccountAdminOrReadOnly]
# Create your views here.
# def index(request):
#     return HttpResponse("Hello! I am a startup or I am a member page")

# def register(request):
#     return HttpResponse("Register page")

# def login(request):
#     return HttpResponse("Login page")
