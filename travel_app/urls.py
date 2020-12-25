from django.urls import path
from travel_app.views import main,content


urlpatterns = [
    path('content/<str:pk>/', content,name='content'),
]