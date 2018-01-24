from django.urls import path
from . import views
app_name='beer'
urlpatterns = [
    path('', views.index,name='index'),
    path('beerinfo/<int:id>',views.beerinfo, name='beerinfo'),
    path('beerinfocomment/<int:id>',views.beerinfocomment,name = 'beerinfocomment'),
    path('beerinfoedit/<int:id>',views.beercommentedit,name='commentedit'),
    path('beerinfodelete',views.beercommentdelete,name='commentdelete'),
    path('membercomment',views.membercomment,name='membercomment'),
    path('beersearch',views.beersearch,name='search'),
    path('beersearchcontent',views.beersearchcontent,name='beersearchcontent'),
    path('beercartadd',views.beercartadd,name='beercartadd'),
    path('cartshow',views.cartshow,name='cartshow'),
]