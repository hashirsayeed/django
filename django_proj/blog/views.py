from django.shortcuts import render
# from django.http import HttpResponse


#sending dummy data using post

posts = [
    {
        'author': 'Hash',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 17, 2024'
    },
    {
        'author': 'Patrick',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 16, 2024'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html')