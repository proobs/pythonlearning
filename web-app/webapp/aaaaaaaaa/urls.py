# needed for django, put it exactly like this
from django.urls import path
# from current folder import views, use it like this, will not take priority if done otherwise
from . import views


urlpatterns = [
    path('', views.index)
]