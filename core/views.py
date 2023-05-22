from django.shortcuts import render, get_object_or_404

from core.models import Blog


def listings(request):
    data = {
        "blog": Blog.objects.all(),
    }
    return render(request, 'listining.html', data)

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    data = {
        "blog": blog,
    }
    return render(request, 'view_blog.html', data)