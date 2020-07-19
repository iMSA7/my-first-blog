from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Cv
from .forms import PostForm, CvForm

def about(request):
    return render(request, 'blog/about.html')

def myCV(request):
    if Cv.objects.all().count() == 1:
        cv = Cv.objects.all()[0]
        return render(request, 'blog/myCV.html', {'cv': cv})
    else:
        return render(request, 'blog/myCV.html')

def cv_new(request):
    if Cv.objects.all().count() == 0:
        if request.method == "POST":
            form = CvForm(request.POST)
            if form.is_valid():
                cv = form.save(commit=False)
                cv.save()
                return redirect('myCV')
        else:
            form = CvForm()
        return render(request, 'blog/cv_new.html', {'form': form})
    else:
        cv = Cv.objects.all()[0]
        return render(request, 'blog/myCV.html', {'cv': cv})

def cv_edit(request):
    if Cv.objects.all().count() == 1:
        cv = Cv.objects.all()[0]
        if request.method == "POST":
            form = CvForm(request.POST, instance=cv)
            if form.is_valid():
                cv = form.save(commit=False)
                cv.save()
                return redirect('myCV')
        else:
            form = CvForm(instance=cv)
        return render(request, 'blog/cv_edit.html', {'form': form})
    else:
        return render(request, 'blog/myCV.html')

def cv_delete(request):
    if request.method == "POST":
        cv = Cv.objects.all()[0]
        cv.delete()
        return redirect('myCV')
    return render(request, 'blog/cv_edit.html')

def sources(request):
    return render(request, 'blog/sources.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.remove()
        return redirect('post_list')
    return render(request, 'blog/post_edit.html')



