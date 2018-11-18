# Generated by Django 2.1.2 on 2018-11-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('comments', '0002_comment_rcvr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rcvr',
        ),
        migrations.AddField(
            model_name='comment',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete='cascade', related_name='receiver', to='auth.Group'),
            preserve_default=False,
        ),
    ]