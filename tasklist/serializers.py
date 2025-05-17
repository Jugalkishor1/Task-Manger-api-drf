from rest_framework import serializers
from .models import Tasklist

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklist
        fields = ['id', 'title', 'description', 'status',]