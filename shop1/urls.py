from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('portfolio/<int:index_id>/', portfolio, name='portfolio'),
    path('contacts/', contacts, name='contacts'),
    path('photo/<int:id>/', photo, name='photo'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]

