from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
   
    path('signup',views.signup,name = 'signup'),
    
    path('login',views.login_view,name = 'login'),
    path('logout',views.logout_view,name='logout'),
    path('userinfo',views.userinfo,name='userinfo'),
    path('userinfoedit',views.userinfoedit,name='userinfoedit'),
    path('resetpwd',views.resetpwd,name='resetpwd'),
    
]
