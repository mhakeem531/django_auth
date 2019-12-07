from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'ostafandy'
urlpatterns = [
    path('signup-ostafandy/', views.signup_ostafandy, name='signup_ostafandy'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='ostafandy/auth/login.html'), name='login'),
    path('home/', views.home, name='home'),
    #path('home_/', views.home_no_logging, name='home_no_logging'),
    path('logout/', views.l_logout, name='logout'),
]
