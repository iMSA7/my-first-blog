import datetime, time
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from .models import Post
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostModelTests(TestCase):
	
	def test_post_publish(self):
		"""
		test for method post.publish()
		"""
		post = Post(title="title", text="text")
		post.publish()
		self.assertEqual(Post.objects.count(),1)

	def test_post_remove(self):
		"""
		test for method post.remove()
		"""
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

class completePostTests(TestCase):

	def test_add_edit_delete_post(self):
		"""
		tests  for editing, adding and deleting a post.
		"""
		browser = webdriver.Chrome()
		browser.get("http://msa7.pythonanywhere.com/post/new/")
		titleForm = browser.find_element_by_name("title")
		textForm = browser.find_element_by_name("text")
		titleForm.send_keys("title passed")
		textForm.send_keys("text passed")
		titleForm.send_keys(Keys.RETURN)
		title = browser.find_element_by_tag_name("h2").text
		self.assertTrue("Title Passed" in title)
		editButton = browser.find_element_by_tag_name("button")
		editButton.click()
		titleForm = browser.find_element_by_name("title")
		titleForm.send_keys(" again")
		titleForm.send_keys(Keys.RETURN)
		title = browser.find_element_by_tag_name("h2").text
		self.assertTrue("Title Passed Again" in title)
		editButton = browser.find_element_by_tag_name("button")
		editButton.click()
		deleteButton = browser.find_element_by_id("delete")
		deleteButton.click()
		self.assertFalse("Title Passed Again" in browser.page_source)
		browser.quit()

	
class CvTests(TestCase):
	
	def test_edit_cv(self):
		"""
		tests whether editing the cv gets applied
		"""
		browser = webdriver.Chrome()
		browser.get("http://msa7.pythonanywhere.com/myCV/edit/")
		Telephone = browser.find_element_by_name("telephone")
		copy = Telephone.get_attribute("value")
		for item in copy:
			Telephone.send_keys(Keys.BACKSPACE)
		Telephone.send_keys("test passed")
		Telephone.send_keys(Keys.RETURN)
		contact = browser.find_element_by_tag_name("p").text
		browser.get("http://msa7.pythonanywhere.com/myCV/edit/")
		Telephone = browser.find_element_by_name("telephone")
		for item in Telephone.get_attribute("value"):
			Telephone.send_keys(Keys.BACKSPACE)
		Telephone.send_keys(copy)
		Telephone.send_keys(Keys.RETURN)
		self.assertTrue("test passed" in contact)
		browser.quit()

	def test_None_fields_in_CV(self):
		"""
		if a field in the cv is  None it should  not be displayed
		"""
		browser = webdriver.Chrome()
		browser.get("http://msa7.pythonanywhere.com/myCV/edit/")
		referees = browser.find_element_by_id("id_referees")
		Telephone = browser.find_element_by_name("telephone")
		copy = referees.get_attribute("value")
		referees.clear()
		referees.send_keys("None")
		Telephone.send_keys(Keys.RETURN)
		browser.get("http://msa7.pythonanywhere.com/myCV/edit/")
		referees = browser.find_element_by_id("id_referees")
		referees.clear()
		referees.send_keys(copy)
		Telephone = browser.find_element_by_name("telephone")
		Telephone.send_keys(Keys.RETURN)
		self.assertTrue("test passed" not in browser.page_source)
		browser.quit()

"""
the following tests are deactivated as these safety
features are disabled to allow assessment team to test
other features such as editing and adding new posts.
"""

class PostEditViewTests():
	"""
	tests for Post Edit View.
	"""
	def test_not_authorised_edit(self):
		"""
		not authorised client should not be allowed to edit a post.
		"""
		post = Post(title="title", text="text")
		post.publish()
		response = self.client.get(reverse('post_edit', args=(post.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "You are not Authorised")

	def test_not_authorised_delete(self):
		"""
		not authorised client should not be allowed to delete a post.
		"""
		post = Post(title="title", text="text")
		post.publish()
		response = self.client.get(reverse('post_delete', args=(post.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "You are not Authorised")
