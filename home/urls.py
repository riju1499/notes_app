from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),

    path('login/',views.LoginInterfaceView.as_view(),name='login'),
    # path('logout/',views.LogoutInterfaceView.as_view(),name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/',views.SignupView.as_view(),name='signup'),
   
   
   
]