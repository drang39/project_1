from django.urls import path
from . import views
app_name='beer'
urlpatterns = [
    path('', views.index,name='index'),
    path('beerinfo/<int:id>',views.beerinfo, name='beerinfo'),
    
    
]