
from django.contrib import admin
from django.urls import path
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name="main"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),
    path('settings', views.settings, name="settings"),
    path('upload', views.upload, name="upload"),
    path('like-post', views.like_Post, name="like-post"),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('follow', views.follow, name="follow"),
    
]


urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)