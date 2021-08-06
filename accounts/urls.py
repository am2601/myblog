from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.registrate_user, name='registration'),
    path('login/', views.login_user, name='login'),
]
