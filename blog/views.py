from django.shortcuts import render


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 15, 2020'
    },
    {
        'author': 'Alexander',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 16, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog\home.html', context)


def about(request):
    return render(request, 'blog\\about.html', {'title': 'About'})
