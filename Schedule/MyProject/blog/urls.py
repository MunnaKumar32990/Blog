from django.urls import path
from. import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/list/', views.post_list, name='post_list'),
]