from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
   
    path('signup',views.signup,name = 'signup'),
    path('update',views.update,name = 'update'),
    path('login',views.login_view,name = 'login'),
    path('logout',views.logout_view,name='logout'),
    
]
