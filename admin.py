from django.contrib import admin

# Register your models here.

from .models import Wine
from .models import Winemaker
from .models import Variety
from .models import Nation


class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'winemaker', 'variety', 'price')


admin.site.register(Wine, WineAdmin)
admin.site.register(Winemaker)
admin.site.register(Variety)
admin.site.register(Nation)