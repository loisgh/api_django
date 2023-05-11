from django.urls import path
from .views import test_response, get_name

urlpatterns = [
    path('test', test_response, name="test"),
    path('getname/<int:id>/', get_name, name="getname"),
]