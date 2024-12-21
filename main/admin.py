from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Phone, Producer, Category


class PhoneAdmin(ModelAdmin):
    filter_horizontal = ('category', 'producer')


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Producer)
admin.site.register(Category)
