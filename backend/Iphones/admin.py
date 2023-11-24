from django.contrib import admin
from . import models


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('color',)}


admin.site.register(models.ProcessorIphone)
admin.site.register(models.ScreenIphone)


@admin.register(models.Iphone)
class IphoneAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'model',
        'image',
        'text',
        # "rom",
        # 'mobile_connection',
        # 'price',
        # 'processor',
        # 'screen',
    )