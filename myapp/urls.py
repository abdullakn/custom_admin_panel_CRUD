from django.urls import path
from .views import *
from . import views


urlpatterns=[

    path('', Registration.as_view(),name="registration"),
    path('login/',Login.as_view(),name="login"),
    path('home/',Home,name="home"),
    path('logout/',Logout,name="logout"),
    path('customadmin/',custom_admin,name='customadmin'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name="delete"),
    path('adduser/',adduser,name='adduser'),
    path('newadmin/',newadmin,name='newadmin'),
    path('adminlogin/',adminlogin,name='adminlogin'),
    path('adminlogout/',adminlogout,name='adminlogout')

]

