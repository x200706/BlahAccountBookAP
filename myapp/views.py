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
    serializer_class = AccountsWithKindsMemoSerializer
    def get(self, request, *args, **kwargs): # self跟request在這邊都是必傳！
        print(kwargs.get('id'))
        if kwargs.get('id') != None: # 查看單筆記帳
            accounts = Account.objects.get(id=kwargs.get('id'))
            serializer = self.serializer_class(accounts, many=False) # 單筆查詢記得給many關閉，不然會警告你"查詢結果是不可迭代的"
            data = serializer.data
            return ResponseTool.success_json_res(data)
        else: # 查看所有記帳
            accounts = Account.objects.all()
            serializer = self.serializer_class(accounts, many=True)
            data = serializer.data
            return ResponseTool.success_json_res(data)

    # 新增單筆記帳
    def post(self, request,*args, **kwargs):
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
    serializer_class = ItemKindsSerializer
    # 查看所有類別
    def get(self, request, *args, **kwargs):
        if kwargs.get('kind') != None: # 查看單個類別
            item_kinds = ItemKinds.objects.get(kind=kwargs.get('kind'))
            serializer = self.serializer_class(item_kinds, many=False)
            data = serializer.data
            return ResponseTool.success_json_res(data)
        else: # 查看所有類別
            item_kinds = ItemKinds.objects.all()
            serializer = self.serializer_class(item_kinds, many=True)
            data = serializer.data
            return ResponseTool.success_json_res(data)

    # 新增單個類別
    def post(self, request):
            data = request.data
            try:
                serializer = self.serializer_class(data=data)
                serializer.is_valid(raise_exception=True)
                with transaction.atomic():
                    serializer.save()
                return ResponseTool.success_json_res({})
            except Exception as e:
                return ResponseTool.exception_json_res(data)