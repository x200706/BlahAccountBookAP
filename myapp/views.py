from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from myapp.serializers import ItemKindsSerializer
from myapp.serializers import AccountSerializer
from myapp.serializers import AccountsWithKindsMemoSerializer
from myapp.models import ItemKinds
from myapp.models import Account
from myapp.response import ResponseTool
import datetime

class AccountView(GenericAPIView):
    # TODO(Crystal) 大姊有的寫法太多餘，改一下唄
    serializer_class = AccountsWithKindsMemoSerializer
    def get(self, request, *args, **kwargs): # self跟request在這邊都是必傳！
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
            return ResponseTool.exception_json_res(e)
   
    # 修改單筆記帳
    def put(self, request,*args, **kwargs):
        data = request.data
        try:
            entity = Account.objects.get(id=kwargs.get('id'))
        except Exception as e:
            return ResponseTool.exception_json_res(e)
        serializer_class = AccountSerializer
        serializer = serializer_class(instance=entity,data=data,partial=False)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
                serializer.save()
        return ResponseTool.success_json_res({})

    # 刪除單筆記帳
    def delete(self, request,*args, **kwargs):
        try:
            accounts = Account.objects.get(id=kwargs.get('id'))
            accounts.delete()
            return ResponseTool.success_json_res({})
        except Exception as e:
            return ResponseTool.exception_json_res(e)
    
class ItemKindsView(GenericAPIView):
    serializer_class = ItemKindsSerializer
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
    def post(self, request, *args, **kwargs):
            data = request.data
            try:
                serializer = self.serializer_class(data=data)
                serializer.is_valid(raise_exception=True)
                with transaction.atomic():
                    serializer.save()
                return ResponseTool.success_json_res({})
            except Exception as e:
                return ResponseTool.exception_json_res(e)
    
    # 修改單個類別desc
    def put(self, request, *args, **kwargs):
        data = request.data
        try:
            entity = ItemKinds.objects.get(kind=kwargs.get('kind'))
        except Exception as e:
            return ResponseTool.exception_json_res(e)
        serializer_class = self.serializer_class
        serializer = serializer_class(instance=entity,data=data,partial=True) # 但沒做不能改pk的限制...
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
                serializer.save()
        return ResponseTool.success_json_res({})
    
class CanvaView(GenericAPIView):
    serializer_class = AccountsWithKindsMemoSerializer
    def current_month_pie(self, request):
        accounts = Account.objects.all()
        data = {}
        return ResponseTool.success_json_res(data)

    def expenditure_bar(self, request):
        accounts = Account.objects.all()
        data = {}
        return ResponseTool.success_json_res(data)

    def income_bar(self, request):
        data = {}
        now = datetime.datetime.now()
        # 收集今年月份
        today_year = now.year
        today_year_months = range(1,now.month+1)
        for today_year_month in today_year_months:
            month_key = '%s_%s' % (today_year, today_year_month)
            data[month_key]=[] # 建立每個月份的list
            accounts = Account.objects.filter(date__year=today_year).filter(date__month=today_year_month).filter(io='INPUT')
            for node in accounts:
                data[month_key].append(node.price)
            # 加總
            data[month_key] = sum(data[month_key])

        # 如果data沒有12個key len(data.keys())；會做這樣的判斷 因為想減少DB連線次數 雖然只有年底會節省到-.-
        if len(data.keys()) < 12:
            # 繼續收集去年月份
            last_year =  int(now.year) -1
            last_year_months = range(now.month+1, 13)
            for last_year_month in last_year_months:
                month_key = '%s_%s' % (last_year, last_year_month)
                data[month_key]=[] # 建立每個月份的list
                accounts = Account.objects.filter(date__year=last_year).filter(date__month=last_year_month).filter(io='INPUT')
                for node in accounts:
                    data[month_key].append(node.price)
                # 加總
                data[month_key] = sum(data[month_key])
        return ResponseTool.success_json_res(data)

    def top_ten_list(self, request):
        accounts = Account.objects.filter(io='OUTPUT').order_by('price')[:10]
        serializer = self.serializer_class(accounts, many=True)
        data = serializer.data
        return ResponseTool.success_json_res(data)

    def total_assets(self, request):
        price_list = []

        input = Account.objects.filter(io='INPUT')
        for node in input:
            price_list.append(node.price)

        output = Account.objects.filter(io='OUTPUT')
        for node in output:
            price_list.append(-node.price) #轉負號

        data = {'value':sum(price_list)}
        return ResponseTool.success_json_res(data)