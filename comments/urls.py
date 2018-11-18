from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.user_comments),
    path('inbox/', views.inbox, name='inbox'),
    path('inbox/received', views.inbox_r, name='inbox_r'),
    path('inbox/sent', views.inbox_s, name='inbox_s'),
    path('groups/<int:group_id>/messages', views.group_messages, name='group_messages'),
    path('inbox/<int:message_id>', views.specific_inbox_message, name='specific_inbox_message'),
    path('inbox/sent/<int:message_id>', views.specific_inbox_s_message, name='specific_inbox_s_message'),
    path('inbox/received/<int:message_id>', views.specific_inbox_r_message, name='specific_inbox_r_message')



]
