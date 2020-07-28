from django.shortcuts import render

posts = [
    {
        'author': 'Ansh Khandelwal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 27,2020'
    },
    {
        'author': 'Kunal Tawde',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 28,2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})


