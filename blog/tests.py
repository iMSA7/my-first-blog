import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Post

class PostModelTests(TestCase):
	"""docstring for PostModelTests"""

	def test_no_published_date(self):
		"""
		If the post is created it should have no publish date
		"""
		post = Post(title="first",text="some content")
		self.assertTrue(hasattr(post, 'published_date'))

	def test_publish(self):
		"""publish should create a publish date and save it"""
		post = Post(title="first",text="some content")
		post.publish
		self.assertEquals(hasattr(post,'published_date'),True)