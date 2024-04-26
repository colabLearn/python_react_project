from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VendorSerializer
from .models import VendorDisc

class VendorView(viewsets.ModelViewSet):
    serializer_class=VendorSerializer
    queryset=VendorDisc.objects.all()
# Create your views here.
