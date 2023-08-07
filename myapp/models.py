from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ItemKinds(models.Model): #一
    kind = models.CharField(primary_key=True, max_length=10)
    desc = models.CharField(max_length=24)
    # color = models.CharField(max_length=20) # v2版才給他們圖表自訂顏色

class Account(models.Model): #對多
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
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

