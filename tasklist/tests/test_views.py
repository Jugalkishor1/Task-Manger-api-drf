from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import Tasklist
import pdb

User = get_user_model()

class TaskListViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass123')
        self.token = RefreshToken.for_user(self.user).access_token
        self.auth_header = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        self.url = reverse('task-list')

    def test_list_all_users_tasks(self):
        task1 = Tasklist.objects.create(user=self.user, title='Task 1')

        response = self.client.get(self.url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], task1.title)


    def test_get_tasks_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_post_task_success(self):
        data = {
            "title": "Test Task",
            "description": "Test task description",
            "status": "not_started"
        }

        response = self.client.post(self.url, data, format='json', **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_post_task_with_invlaid_attr(self):
        data = {
            "title": "",
            "status": "not_started"
        }

        response = self.client.post(self.url, data, format='json', **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)


class TaskDetailView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass123')
        self.token = RefreshToken.for_user(self.user).access_token
        self.auth_header = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

    def test_get_task_details(self):
        task1 = Tasklist.objects.create(user=self.user, title='Task 1')
        url = reverse('task-detail', kwargs={'pk': task1.id})
        
        response = self.client.get(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], task1.title)
    
    
    def test_try_to_get_non_existing_task(self):
        task1 = Tasklist.objects.create(user=self.user, title='Task 1')
        url = reverse('task-detail', kwargs={'pk': task1.id + 1})
        
        response = self.client.get(url, **self.auth_header)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Task not found")

    
    def test_update_task(self):
        task1 = Tasklist.objects.create(user=self.user, title='Test task')
        url = reverse("task-detail", kwargs={'pk': task1.id})

        response = self.client.put(url, **self.auth_header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test task")


    def test_try_to_update_non_existing_task(self):
        task1 = Tasklist.objects.create(user=self.user, title='Task 1')
        url = reverse('task-detail', kwargs={'pk': task1.id + 1})
        
        response = self.client.put(url, **self.auth_header)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Task not found.")
    
    def test_update_with_invlaid_params(self):
        task1 = Tasklist.objects.create(user=self.user, title='Task 1')
        url = reverse('task-detail', kwargs={'pk': task1.id})
        data = {
            "title": ""
        }
        response = self.client.put(url, data,**self.auth_header)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_delete_task(self):
        task1 = Tasklist.objects.create(user=self.user, title='Task 1')
        url = reverse('task-detail', kwargs={'pk': task1.id})
        
        response = self.client.delete(url, **self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data['message'], "Task deleted.")

    
    def test_delete_non_existing_task(self):
        task1 = Tasklist.objects.create(user=self.user, title='Task 1')
        url = reverse('task-detail', kwargs={'pk': task1.id + 1})
        
        response = self.client.delete(url, **self.auth_header)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "Task not found.")


class CompletedTaskListView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass123')
        self.token = RefreshToken.for_user(self.user).access_token
        self.auth_header = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

    def test_get_all_completed_tasks(self):
        task1 = Tasklist.objects.create(user=self.user, title='Task 1', status="completed")

        url = reverse('completed')
        
        response = self.client.get(url, **self.auth_header)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], task1.title)