from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView
)
from .models import Post


class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body']

class AboutView(TemplateView):
    template_name = "about.html"
