# Generated by Django 4.2.1 on 2023-06-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_post_number_of_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
