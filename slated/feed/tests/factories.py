import factory
from django.conf import settings
from django.contrib.auth.hashers import make_password

from feed.models import FeedItem, RegisteredUser

TEST_USER_PASSWORD = 'P4ssw0rd'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Sequence(lambda n: 'user_{0}'.format(n))
    password = make_password(TEST_USER_PASSWORD)


class FeedItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FeedItem

    content = factory.Faker('text')
    user = factory.SubFactory(UserFactory)


class RegisteredUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RegisteredUser

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def tracking(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for tracking_by in extracted:
                self.tracking.add(tracking_by)
