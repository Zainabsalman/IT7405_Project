from django.urls import path 
from app import views 

app_name = "app" 

urlpatterns = [ 
    path('', views.app_list,name="homepage"),
    path("app_details/<int:id>/",views.app_details, name='app_details'),
    path('addRouter',views.addRouter, name='addRouter'),
    path('search', views.search, name="search"),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    ]
    