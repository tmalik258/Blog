from django.test import TestCase, TransactionTestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.

class APIUsersTest (TransactionTestCase):
	"""Account Retrieve"""

	def setUp(self):
		self.client = APIClient()
	
	def test_registration_new_user(self):
		"""
			Create a user using dj-rest-auth and get auth key in response
		"""
		response = self.client.post('/api/v1/dj-rest-auth/registration/', {
			'username': 'testuser',
			'email': 'testuser@example.com',
			'password1': 'outlook25',
			'password2': 'outlook25',
		})

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertIn('key', response.data)

		User = get_user_model()
		self.assertTrue(User.objects.filter(username='testuser').exists())