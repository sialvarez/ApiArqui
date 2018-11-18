from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.specific_user),
    path('<int:user_id>/groups', views.user_groups),
    path('delete', views.delete_user),
    path('login', views.user_login),
    path('logout', views.user_logout)
]
