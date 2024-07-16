from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post

# Create your tests here.

class BlogTests(TestCase):
	@classmethod
	def setUpTestData(cls) -> None:
		cls.user = get_user_model().objects.create_user(
			username="tmalik",
			email='test@gmail.com',
			password='secret123'
		)
		cls.post = Post.objects.create(
			author=cls.user,
			title='A good title',
			body="Nice body content"
		)
	
	def test_post_model(self):
		self.assertEqual(self.post.author.username, "tmalik")
		self.assertEqual(self.post.title, "A good title")
		self.assertEqual(self.post.body, "Nice body content")
		self.assertEqual(str(self.post), "A good title")