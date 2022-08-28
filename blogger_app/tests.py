from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Blog


class BlogTests(TestCase):

    def blog_setup(self):
        self.blog = Blog.objects.create(title='First Blog', subject=None, post_date='8/28/2022', author='Brendon')

    def test_blog_name(self):
        self.assertEqual(f'{self.blog.title}', 'First Blog')

    def test_not_blog_name(self):
        self.assertIsNot(f'{self.blog.title}', 'Second Blog')

    def test_subject(self):
        self.assertIs(self.blog.subject, None)

    def test_post_date(self):
        current_date = 
        self.assertIs(self.blog.post_date, )