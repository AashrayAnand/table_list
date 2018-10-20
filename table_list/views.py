from django.shortcuts import render
from table_list.models import table_items
from table_list.serializers import tableSerializer
from rest_framework import generics
# Create your views here.
class TableListCreate(generics.ListCreateAPIView):
    queryset = table_items.objects.all()
    serializer_class = tableSerializer
