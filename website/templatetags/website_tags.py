from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter   
def snippet(value,arg=10):
    return value[:arg] + '...'

@register.inclusion_tag('website/latest-posts.html')
def latestposts(arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}