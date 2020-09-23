from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from data.models import Data

admin.site.register(Data, DraggableMPTTAdmin)