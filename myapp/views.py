from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from myapp.serializers import ItemKindsSerializer
from myapp.serializers import AccountSerializer
from myapp.serializers import AccountsWithKindsMemoSerializer
from myapp.models import ItemKinds
from myapp.models import Account
from myapp.response import ResponseTool

class AccountView(GenericAPIView):
    queryset = Account.objects.all()
    def get(self, id):
        accounts = self.get_queryset()
        serializer_class = AccountsWithKindsMemoSerializer
        serializer = serializer_class(accounts, many=True)
        data = serializer.data
        return ResponseTool.success_json_res(data)

    # 新增單條記帳
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            serializer_class = AccountSerializer
            serializer = serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            return ResponseTool.success_json_res({})
        except Exception as e:
            return ResponseTool.exception_json_res(data)
    
class ItemKindsView(GenericAPIView):
    queryset = ItemKinds.objects.all()
    serializer_class = ItemKindsSerializer
    # 查看所有類別
    def get(self, kind):
        item_kinds = self.get_queryset()
        serializer = self.serializer_class(item_kinds, many=True)
        data = serializer.data
        return ResponseTool.success_json_res(data)
    # 查看單個類別

    # 新增單個類別
    def post(self, request, *args, **kwargs):
            data = request.data
            try:
                serializer = self.serializer_class(data=data)
                serializer.is_valid(raise_exception=True)
                with transaction.atomic():
                    serializer.save()
                return ResponseTool.success_json_res({})
            except Exception as e:
                return ResponseTool.exception_json_res(data)