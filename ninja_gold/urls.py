from django.urls import path     
from . import views

urlpatterns =[
    path('',views.index),    
    path('/',views.index),    
    path('process_money/<str:ubi>/',views.process_money),  
    #path('process_money/<str:ubi>/',views.process_money),
]