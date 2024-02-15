from django.urls import path

from .views import *

urlpatterns = [
    path('',example_view),
    path('login/', login_view),
    path('signup/', signup_view),
    path('message/', message_view),
]