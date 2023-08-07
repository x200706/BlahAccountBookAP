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
    kind_desc = serializers.CharField(source='kind.desc', read_only=True)  # 添加 kind_desc 字段

    class Meta:
        model = Account
        fields = '__all__'