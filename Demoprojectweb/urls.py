from django . urls import path
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('index',views.home,name='home'),
    path('register',views.register,name='register'),
    path('loginvalidate',views.loginvalidate,name='loginvalidate'),
    ]
    
