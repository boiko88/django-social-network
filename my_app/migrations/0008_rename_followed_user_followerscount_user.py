# Generated by Django 4.2.1 on 2023-06-07 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_followerscount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followerscount',
            old_name='followed_user',
            new_name='user',
        ),
    ]