from myapp.models import Account 
from myapp.models import ItemKinds 

from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class ItemKindsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemKinds
        fields = '__all__'

class AccountsWithKindsMemoSerializer(serializers.ModelSerializer):
    item_kinds = ItemKindsSerializer(many=True, read_only= True)
    class Meta:
        model = Account
        fields = ['item_kinds','desc']