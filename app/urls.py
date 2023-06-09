from django.urls import path
from .views import home, success

urlpatterns = [
    path('/<str:obj1>/<int:obj2>', home, name='home'),
    path('success/<str:obj1>/<int:obj2>', success, name='success'),
]
8