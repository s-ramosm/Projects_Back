# Generated by Django 4.1 on 2024-04-16 18:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_remove_task_user_owner_member'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Owner',
            new_name='OwnersTasks',
        ),
    ]
