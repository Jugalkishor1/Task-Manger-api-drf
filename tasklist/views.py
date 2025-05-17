from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import Tasklist
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.db import models


class TaskListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Tasklist.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Tasklist.objects.get(id=pk, user=request.user)
        except Tasklist.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            task = Tasklist.objects.get(id=pk, user=request.user)
        except Tasklist.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = Tasklist.objects.get(id=pk, user=request.user)
        except Tasklist.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({'message': 'Task deleted.'}, status=status.HTTP_204_NO_CONTENT)


class CompletedTaskListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        completed_tasks = Tasklist.objects.filter(user=request.user, status='completed')
        serializer = TaskSerializer(completed_tasks, many=True)
        return Response(serializer.data)


class TaskSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '')
        results = Tasklist.objects.filter(user=request.user).filter(
            models.Q(title__icontains=query) | models.Q(description__icontains=query)
        )
        serializer = TaskSerializer(results, many=True)
        return Response(serializer.data)
