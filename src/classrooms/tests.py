from django.test import TestCase, Client
from django.urls import reverse
from .models import Classroom

class ClassroomTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.classroom = Classroom.objects.create(name='Room 101', capacity=30, location='Building A')

    def test_list_classrooms(self):
        response = self.client.get(reverse('list_classrooms'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Room 101')

    def test_create_classroom(self):
        response = self.client.post(reverse('create_classroom'), {
            'name': 'Room 102',
            'capacity': 25,
            'location': 'Building B'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Classroom.objects.filter(name='Room 102').exists())

    def test_edit_classroom(self):
        response = self.client.post(reverse('edit_classroom', args=[self.classroom.id]), {
            'name': 'Room 101 Updated',
            'capacity': 35,
            'location': 'Building A'
        })
        self.assertEqual(response.status_code, 302)
        self.classroom.refresh_from_db()
        self.assertEqual(self.classroom.name, 'Room 101 Updated')

    def test_delete_classroom(self):
        response = self.client.post(reverse('delete_classroom', args=[self.classroom.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Classroom.objects.filter(id=self.classroom.id).exists())