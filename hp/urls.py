from django.urls import path
from .views import index , register , user_login , user_logout , contact

url_patterns = [
    path('' , index, name = 'home'),
    path('register/' , register , name = 'register'),
    path('login/' , user_login , name='login'),
    path('logout/' , user_logout , name='logout') ,
    path('contact/' , contact , name = 'contact') ,
    # path('example/' , example , name='example'),
    # path('ex/' , RetrivingData , name='Retriving'),
    # path('user/' , UserRetrive , name='user'),
    # path('all/' , showForm , name='show') ,
    # path('student/' , student , name='student') ,
    # path('ano/' , anothe , name = 'another')
]