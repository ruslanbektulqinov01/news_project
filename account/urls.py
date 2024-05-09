from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('verify/<str:id>/', verification, name='verify'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('new_password/<str:id>/', new_password, name='new_password'),
]
