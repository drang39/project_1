from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
  
    path('',views.index,name = 'index'),
    path('create',views.create,name = 'create'),
    path('update',views.update,name = 'update'),
    path('updatedb',views.updatedb,name = 'updatedb'),
    path('delete',views.delete,name='delete'),
    
]
