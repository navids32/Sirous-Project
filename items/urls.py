from django.urls import path
from .views import TestApp, TestView

urlpatterns = [
    path('testapp/', TestApp),
    path('testview/', TestView),
]
