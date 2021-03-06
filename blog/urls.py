from django.urls import path
from . import views

urlpatterns = [
	path('', views.about, name='about'),
	path('sources/', views.sources, name='sources'),
    path('blog/', views.post_list, name='post_list'),
    path('myCV/', views.myCV, name='myCV'),
    path('myCV/new/', views.cv_new, name='cv_new'),
    path('myCV/edit/', views.cv_edit, name='cv_edit'),
    path('myCV/edit/delete/', views.cv_delete, name='cv_delete'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/edit/delete/', views.post_delete, name='post_delete'),
]