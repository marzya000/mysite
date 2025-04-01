from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request,pid):
    post = get_object_or_404(Post,pk=pid,status=1)   
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

def test(request):
   # post = Post.objects.get(id=pid) 
   # post = get_object_or_404(Post,pk=pid,status=1)   
   # context = {'post':post}
    return render(request,'test.html')