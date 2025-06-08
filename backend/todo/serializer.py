from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        field = ('id', 'title', 'description', 'completed')
        fields = '__all__'
