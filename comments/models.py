from django.db import models
from django.contrib.auth.models import User, Group


class Comment(models.Model):
    sender = models.ForeignKey(User, on_delete="cascade")
    receiver = models.ForeignKey(Group, on_delete="cascade")
    msg_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, default=None)

# Create your models here.
