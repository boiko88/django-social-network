from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime


User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='default-profile-picture.png')
    location = models.CharField(max_length=200, blank=True)
    
    
    def __str__(self):
        return self.user.username
    
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    likes_number = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.user
    

class LikePost(models.Model):
    post_id = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username