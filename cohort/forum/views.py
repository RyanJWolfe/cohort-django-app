from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from forum.models import Topic


class TopicListView(ListView):

    model = Topic
    paginate_by = 100
    allow_empty = False
    template_name = 'topic_list.html'


class TopicDetailView(DetailView):

    model = Topic
    template_name = 'topic_detail.html'


class TopicCreateView(CreateView):

    model = Topic
    fields = ['title']
    template_name = 'topic_form.html'
