from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import timezone
from .models import Post


# Create your views here.


def base(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts}
    return render(request, 'MyApp/base.html', context)


def test(request):
    return render_to_response('MyApp/test.html')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts}
    return render(request, 'MyApp/post_list.html', context)


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    context = {'posts': posts}
    return render(request, 'MyApp/post_detail.html', context)
