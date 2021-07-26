from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),	   
    path('blogs/new', views.new),	   
    path('blogs', views.root),	
    path('blogs/create', views.create),	
    path('blogs/<int:my_val>', views.show),
    path('blogs/<int:my_val>/edit', views.edit),
    path('blogs/<int:my_val>/delete', views.destroy),
    path('blogs/json', views.json),
    ]