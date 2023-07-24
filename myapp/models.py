from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ItemKinds(models.Model): #一
    kind = models.CharField(primary_key=True, max_length=10) # 假裝綜合所得稅代號是"iitax"，好吧給10個字元
    desc = models.CharField(max_length=24) # "綜合所得稅"估15字，給的24好了
    # color = models.CharField(max_length=20) # v2版才給他們圖表自訂顏色

class Account(models.Model): #對多
    id = models.AutoField(primary_key=True) # 其實好像不用寫也有齁
    item_name = models.CharField(max_length=50) # "亞尼克蛋糕捲"這樣的字串估18個字元長度 "Cherry紅軸靜音鍵盤"估6+18=24，給54好了，最多18個UTF8字元
    date = models.DateField()
    class IorO(models.TextChoices):
        OUTPUT = 'OUTPUT', _('支出')
        INPUT = 'INPUT', _('收入')
    io = models.CharField(
        max_length=6,
        choices=IorO.choices,
        default=IorO.OUTPUT,
    )
    kind = models.ForeignKey('ItemKinds',  on_delete=models.CASCADE)

