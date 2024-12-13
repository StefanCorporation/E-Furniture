from django.contrib import admin
from goods.models import Categories, Products


# Register your models here.


@admin.register(Categories)
class CategorysAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Products)
class ProdusctsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}