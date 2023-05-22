from django.test import TestCase
from django.urls import reverse
from .models import Blog

class BlogTests(TestCase):
    def setUp(self):
        Blog.objects.create(title='test', content='test')

    def test_string_representation(self):
        blog = Blog(title='test')
        self.assertEqual(str(blog), blog.title)

    def test_blog_content(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f'{blog.title}'
        self.assertEqual(expected_object_name, 'test')

    def test_blog_list_view(self):
        response = self.client.get(reverse('listings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
        self.assertTemplateUsed(response, 'listings.html')

    def test_blog_detail_view(self):
        response = self.client.get('/1/')
        no_response = self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test')
        self.assertTemplateUsed(response, 'view_blog.html')

# Create your tests here.
