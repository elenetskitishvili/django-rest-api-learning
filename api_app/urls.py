from django.urls import path
from .views import ItemListCreate, ItemDetail, hello_world

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('hello/', hello_world, name='hello-world'),
]
