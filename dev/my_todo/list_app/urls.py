from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "App"

urlpatterns = [path('', views.home_view, name='home'),]

