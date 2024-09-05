from django.urls import path, include

from .views import index

urlpatterns = [
    path('<str:search_item>', index)
]
