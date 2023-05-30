from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "App"

urlpatterns = [
    # path('', views.home_view, name='home'),
    path('create_project/', views.create_project, name='create_project'),
    path('delete/', views.delete_view, name='delete'),
    path('', views.project_lists_view, name='home')
]

