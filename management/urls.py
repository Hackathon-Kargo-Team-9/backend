from django.urls import path
from .views import DriverAPIView
app_name = 'management'
urlpatterns = [
    path('driver', DriverAPIView.as_view()),
]