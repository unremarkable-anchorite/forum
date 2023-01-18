from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import AddPostForm, NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def homePage(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "app/home.html", {
        'posts': posts
    })

def addPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.userPost = request.user
            form.save()
        return redirect("homePage")
    else:
        form = AddPostForm()

    return render(request, "app/addpost.html", {
        'form': form
    })


def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.userPost:
        if request.method == "POST":
            Post.objects.filter(pk=pk).delete()
            return redirect("homePage")

    return render(request, "app/deletepost.html", {
        'post': post
    })


def detailPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "app/detailpost.html", {
        'post': post
    })

def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = AddPostForm(request/POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detailPost", pk=post.pk)
    else:
        form = AddPostForm()
    return render(request, "app/editpost.html", {
        'post': post,
        'form': form
    })

def signIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect("homePage")
            #messege
            else:
                pass
            #message
    else:
        form = AuthenticationForm()
    return render(request, "user/signin.html", {
        'form': form
    })

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # message
            return redirect("homePage")
    else:
        form = NewUserForm()
    return render(request, "user/signup.html", {
        'form': form
    })

def logOut(request):
    logout(request)
    #message
    return redirect("homePage")