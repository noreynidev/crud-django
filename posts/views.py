from django.shortcuts import render, get_object_or_404, redirect
from .models import PostModel
from .forms import PostForm
# Create your views here.
def index(request):
    posts = PostModel.objects.all()[:3]
    return render(request, 'posts/index.html', {'posts':posts})

def listings(request):
    posts = PostModel.objects.all()
    return render(request, 'posts/listings.html', {'posts':posts})

def details(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    return render(request, 'posts/details.html', {'post':post})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:listings')
        else:
            form = PostForm(request.POST)
            return render(request, 'posts/create.html', {'form':form})
    else:
        form = PostForm()
        return render(request, 'posts/create.html', {'form':form})

def update(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('posts:listings')
    else:
        form = PostForm(instance=post)
        return render(request, 'posts/update.html', {'post':post, 'form':form})

def delete(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:listings')
    return render(request, 'posts/delete.html', {'post':post})