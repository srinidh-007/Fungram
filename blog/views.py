from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'srinidh',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 01, 2021' 
    },
    {
        'author': 'koushik',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 02, 2021' 
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)
def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})   