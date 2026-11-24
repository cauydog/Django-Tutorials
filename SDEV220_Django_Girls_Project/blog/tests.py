from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Post


class PostModelTests(TestCase):
    def test_post_can_be_published(self):
        user = get_user_model().objects.create_user(username='student', password='test-only-password')
        post = Post.objects.create(author=user, title='My first post', text='Hello Django!')
        self.assertIsNone(post.published_date)
        post.publish()
        post.refresh_from_db()
        self.assertIsNotNone(post.published_date)
        self.assertLessEqual(post.published_date, timezone.now())
