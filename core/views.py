from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
	authentication_class = [BasicAuthentication]
	permission_class = [IsAuthenticated]
	queryset = Task.objects.all()
	serializer_class = TaskSerializer