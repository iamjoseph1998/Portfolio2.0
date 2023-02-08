from django.urls import path
from app.views import *


app_name = 'app'


urlpatterns = [
    path('get-profile/', GetProfile.as_view(), name='get-profile'),
    path('get-education/', GetEducation.as_view(), name='get-education'),
]