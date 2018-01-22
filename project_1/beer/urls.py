from django.urls import path
from . import views
app_name='beer'
urlpatterns = [
    path('', views.index,name='index'),
    path('beerinfo/<int:id>',views.beerinfo, name='beerinfo'),
    path('beerinfocomment/<int:id>',views.beerinfocomment,name = 'beerinfocomment'),
    path('beerinfoedit/<int:id>',views.beerinfoedit,name='edit'),
    path('beerinfodelete',views.beerinfodelte,name='delete')
]