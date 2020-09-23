from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from dataowner.models import DataOwner

class Data(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    created_by = models.ForeignKey(DataOwner, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    class MPTTMeta:
        order_insertion_by = ['date']

    def __str__(self):
        return self.name


