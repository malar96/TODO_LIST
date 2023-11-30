# views.py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
def taskList(request):
    return HttpResponse('To Do List')

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
