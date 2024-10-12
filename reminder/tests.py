from django.test import TestCase
from .models import Event
from datetime import date, time

from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Event
from datetime import date, time

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

class EventModelTest(TestCase):
    def test_create_event(self):
        event = Event.objects.create(
            title="Test Event",
            description="This is a test event",
            date=date(2024, 10, 15),
            time=time(14, 0),
            category="Work"
        )
        self.assertEqual(event.title, "Test Event")
        self.assertEqual(event.category, "Work")

class EventAPITest(APITestCase):
    def test_create_event(self):
        url = reverse('event-list-create')
        data = {
            "title": "Test API Event",
            "description": "API test description",
            "date": "2024-10-15",
            "time": "14:00",
            "category": "Personal",
            "recurrence": "daily"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().title, "Test API Event")

class EventUpdateDeleteTest(APITestCase):
    def setUp(self):
        self.event = Event.objects.create(
            title="Test Event",
            description="This is a test event",
            date=date(2024, 10, 15),
            time=time(14, 0),
            category="Work"
        )
        self.url = reverse('event-detail', args=[self.event.id])

    def test_update_event(self):
        data = {
            "title": "Updated Test Event",
            "description": "Updated description",
            "date": "2024-10-20",
            "time": "15:00",
            "category": "Work"
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.event.refresh_from_db()
        self.assertEqual(self.event.title, "Updated Test Event")

    def test_delete_event(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Event.objects.count(), 0)

class EventTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_nonexistent_event_returns_404(self):
        response = self.client.get('/events/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)