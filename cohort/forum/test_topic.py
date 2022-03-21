import factory.django
import pytest
from django.contrib.auth.models import User

from forum.models import Topic


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    username = factory.Faker('user_name')


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    title = factory.Faker('sentence')
    created_by = factory.SubFactory(UserFactory)


@pytest.mark.django_db
def describe_topic():
    def exists():
        TopicFactory()

    def saves_its_fields():
        topic = TopicFactory()

        sut = Topic.objects.get(pk=topic.id)

        assert sut.title == topic.title
        assert sut.created_by == topic.created_by