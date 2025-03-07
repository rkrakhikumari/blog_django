from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.

# List all posts (READ)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

# View a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html', {'post': post})

#create a new post
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog/post_form.html')

#update an existing post
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect('post_list')
    return render(request, 'blog/post_form.html', {'post':post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post':post})