from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the list view after creating a post
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

# View for editing an existing post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the list view after editing the post
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

# View for deleting a post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # Redirect to the list view after deleting the post
    return render(request, 'post_confirm_delete.html', {'post': post})