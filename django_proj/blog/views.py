from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse


#sending dummy data using post

# posts = [
#     {
#         'author': 'Hash',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'January 17, 2024'
#     },
#     {
#         'author': 'Patrick',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'January 16, 2024'
#     }
# ]

# Create your views here.

def home(request):
    context = {
        # 'posts': posts
        'posts' : Post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post