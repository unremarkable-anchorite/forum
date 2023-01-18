from django.shortcuts import render

def homePage(request):
    return render(request, "app/home.html")

def addPost(request):
    return render(request, "app/addpost.html")

def deletePost(request):
    return render(request, "app/deletepost.html")

def detailPost(request):
    return render(request, "app/detailpost.html")

def editPost(request):
    return render(request, "app/editpost.html")

def signIn(request):
    return render(request, "user/signin.html")

def signUp(request):
    return render(request, "user/signup.html")

def logOut(request):
    test = "test"