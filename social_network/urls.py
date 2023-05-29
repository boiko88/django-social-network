
from django.contrib import admin
from django.urls import path
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainPage, name="main"),
    path('signup', views.signup, name="signup"),
]


urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)