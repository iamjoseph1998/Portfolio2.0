from django.urls import path
from app.views import *


app_name = 'app'


urlpatterns = [
    path('add-profile/', AddProfile.as_view(), name='add-profile'),
]