from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .factories import UserFactory, FeedItemFactory


class TestFeed(APITestCase):
    def setUp(self):
        self.url = reverse('feed:list')
        self.user = UserFactory()

        self.posts = FeedItemFactory.create_batch(5)
        self.my_posts = FeedItemFactory.create_batch(5, user=self.user)
        # tracked by me
        for post in self.posts[:2]:
            self.user.registered_user.tracking.add(post.user.registered_user)

        # tracking me
        for post in self.posts[2:]:
            post.user.registered_user.tracking.add(self.user.registered_user)

    def test_permissions(self):
        """
        Anonymous user doesn't have access to feed
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_all_post(self):
        """
        User gets all posts
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('{}?post=all'.format(self.url))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), len(self.posts) + len(self.my_posts))
        self.assertEqual(response.json(), [{'pk': post.pk, 'content': post.content, 'username': post.user.username}
                                           for post in self.posts + self.my_posts])

    def test_my_post(self):
        """
        User gets his posts
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('{}?post=my'.format(self.url))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), len(self.my_posts))
        self.assertEqual(response.json(), [{'pk': post.pk, 'content': post.content, 'username': post.user.username}
                                           for post in self.my_posts])

    def test_tracking_post(self):
        """
        User gets posts of everyone who he's tracking
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('{}?post=tracking'.format(self.url))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), len(self.my_posts) + 2)
        self.assertEqual(response.json(), [{'pk': post.pk, 'content': post.content, 'username': post.user.username}
                                           for post in self.my_posts + self.posts[:2]])

    def test_default_filter(self):
        """
        Return all posts by default
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), len(self.posts) + len(self.my_posts))
        self.assertEqual(response.json(), [{'pk': post.pk, 'content': post.content, 'username': post.user.username}
                                           for post in self.posts + self.my_posts])
