from myapp.models import Account 
from myapp.models import ItemKinds 

from rest_framework import serializers
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class ItemKindsSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, read_only=True)  # Change 'kind' to 'accounts'
    
    class Meta:
        model = ItemKinds
        fields = ['accounts', 'desc']  # Add 'desc' field to the serializer