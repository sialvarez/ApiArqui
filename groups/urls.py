from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:group_id>', views.specific_group),
    path('<int:group_id>/users', views.users_of_group),
    path('<int:group_id>/remove', views.remove_users),
    path('<int:group_id>/delete', views.delete_group)
]