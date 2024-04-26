from rest_framework import serializers
from .models import VendorDisc

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDisc
        fields = ('id', 'companyName','street_address', 'city', 'state', 'zip_postal_code', 'country', 'vendorID',  'email',  'telephone') 
  