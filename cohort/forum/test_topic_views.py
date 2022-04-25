import pytest
from django.http import Http404
from django.test import RequestFactory

from forum.test_topic import TopicFactory
from forum.views import TopicListView


@pytest.mark.django_db
def describe_a_topic_list_view():
    @pytest.fixture
    def view_class():
        return TopicListView()

    @pytest.fixture
    def view():
        return TopicListView.as_view()

    @pytest.fixture
    def http_request():
        return RequestFactory().get("/topics/")

    def it_exists():
        assert TopicListView()

    def describe_with_no_topics():
        def it_returns_a_404_response(http_request):
            with pytest.raises(Http404):
                TopicListView.as_view()(http_request)

        def it_responds_with_a_404_from_its_url(client):
            response = client.get("/topics/")
            assert response.status_code == 404

    def describe_with_topics():
        @pytest.fixture
        def topics():
            return TopicFactory.create_batch(5)

        def it_returns_a_200_response(http_request, topics):
            response = TopicListView.as_view()(http_request)
            assert response.status_code == 200

        def it_returns_topics_in_our_template_context(http_request, topics, view_class):
            view_class.setup(http_request)
            view_class.get(http_request)

            context = view_class.get_context_data()

            assert list(context['object_list']) == topics

        def it_responds_with_a_200_from_its_url(client, topics):
            response = client.get("/topics/")
            assert response.status_code == 200
            assert list(response.context_data['object_list']) == topics
