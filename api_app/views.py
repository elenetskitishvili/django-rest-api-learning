from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

# Class-Based Views (CBVs)
class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Function-Based View (FBV)
@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})
