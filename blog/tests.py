import datetime
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Post


class PostModelTests(TestCase):

	def test_post_publish(self):
		post = Post(title="title", text="text")
		post.publish()
		self.assertEqual(Post.objects.count(),1)

	def test_post_remove(self):
		post = Post(title="title", text="text")
		post.publish()
		self.assertEqual(Post.objects.count(),1)
		post.remove()
		self.assertEqual(Post.objects.count(),0)

class PostListViewTests(TestCase):

	def test_no_posts(self):
		"""
		If no posts exist.
		"""
		response = self.client.get(reverse('post_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "More posts are coming soon")
		self.assertQuerysetEqual(response.context['posts'], [])

	def test_one_post(self):
		"""
		If a post exists.
		"""
		post = Post(title="title", text="text")
		post.publish()
		response = self.client.get(reverse('post_list'))
		self.assertQuerysetEqual(response.context['posts'],['<Post: title>'])

	def test_two_posts(self):
		"""
		adding two posts 
		"""
		post = Post(title="title", text="text")
		post.publish()
		post2 = Post(title="title2", text="text")
		post2.publish()
		response = self.client.get(reverse('post_list'))
		self.assertQuerysetEqual(response.context['posts'],['<Post: title>','<Post: title2>'])


class PostEditViewTests(TestCase):
	"""tests for Post Edit View"""
	def test_not_authorised_edit(self):
		"""
		not authorised client should not be allowed to edit a post and an appropriate message will be displayed
		"""
		post = Post(title="title", text="text")
		post.publish()
		response = self.client.get(reverse('post_edit', args=(post.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "You are not Authorised")

	def test_not_authorised_delete(self):
		post = Post(title="title", text="text")
		post.publish()
		response = self.client.get(reverse('post_delete', args=(post.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "You are not Authorised")
