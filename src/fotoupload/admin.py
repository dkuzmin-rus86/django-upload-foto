from django.contrib import admin
from .models import Foto


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'info', 'item', )
    search_fields = ('info',)
    ordering = ('pk',)


