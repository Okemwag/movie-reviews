from django.contrib import admin
from django.urls import path
from movie import views as MovieViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieViews.home, name='home'),
    path('about/', MovieViews.about, name='about'),
    path('signup/', movieViews.signup, name='signup'),
]
