from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('icon/<int:id>', views.icon, name='icon'),
    path('publications/', views.publications, name='publications'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('delete/<int:id>', views.delete_comment, name='delete'),
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('create/publications/', views.create_publications, name='create_publications'),
    path('update/<int:id>', views.update, name='update')
]