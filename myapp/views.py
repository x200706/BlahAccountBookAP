from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from myapp.serializers import ItemKindsSerializer
from myapp.serializers import AccountSerializer
from myapp.models import ItemKinds
from myapp.models import Account
from myapp.response import ResponseTool

class AccountView(GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = ItemKindsSerializer

    def get(self, request, *args, **kwargs):
        accounts = self.get_queryset()
        serializer_class = AccountSerializer
        serializer = serializer_class(accounts, many=True)
        data = serializer.data
        return ResponseTool.jsob_res(data)

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            serializer_class = AccountSerializer
            serializer = serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
            response_data = {
                "message": "成功",
                "code": "SUCCESS",
                "data": data
            }
        except Exception as e:
            response_data = {
                "message": "Something throw a exception.",
                "code": "SOME_EXCEPTION",
                "error": str(e)
            }
        return JsonResponse(response_data)
    
class ItemKindsView(GenericAPIView):
    queryset = ItemKinds.objects.all()
    serializer_class = ItemKindsSerializer
    def get(self, request, *args, **kwargs):
        item_kinds = self.get_queryset()
        serializer = self.serializer_class(item_kinds, many=True)
        data = serializer.data
        return ResponseTool.jsob_res(data)
    
    def post(self, request, *args, **kwargs):
            data = request.data
            try:
                serializer = self.serializer_class(data=data)
                serializer.is_valid(raise_exception=True)
                with transaction.atomic():
                    serializer.save()
                data = serializer.data
                response_data = {
                    "message": "成功",
                    "code": "SUCCESS",
                    "data": data
                }
            except Exception as e:
                response_data = {
                    "message": "Something throw a exception.",
                    "code": "SOME_EXCEPTION",
                    "error": str(e)
                }
            return JsonResponse(response_data)