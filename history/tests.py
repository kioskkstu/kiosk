from django.test import TestCase
from .models import *
from rest_framework import status
from django.urls import reverse


class HistoryModelTests(TestCase):
    @classmethod
    def setUp(self):
        self.old_cnt = History.objects.count()
        self.history = History.objects.create(name='test', text='test')

    def test_model_create_History(self):
        self.new_cnt = History.objects.count()
        self.assertNotEqual(self.old_cnt, self.new_cnt)

    def test_api_get_History(self):
        response = self.client.get(
            reverse('history'),
            kwarge={'pk': self.history.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.history)
