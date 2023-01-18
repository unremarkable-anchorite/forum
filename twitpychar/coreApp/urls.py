from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('post/view/<int:pk>/', views.detailPost, name='detailPost'),
    path('post/add/', views.addPost, name='addPost'),
    path('post/delete/<int:pk>/', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>/', views.editPost, name='editPost'),
    path('user/signup/', views.signUp, name='signUp'),
    path('user/signin/', views.signIn, name='signIn'),
    path('user/logout/', views.logOut, name='logOut'),
]