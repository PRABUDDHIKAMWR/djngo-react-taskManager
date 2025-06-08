from django.shortcuts import render

from rest_framework import viewsets
from .serializer import ToDoSerializer
from .models import ToDo

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


