from django.contrib import admin
from .models import Product, Store, ProductStore

class ProductStoreInline(admin.TabularInline):
    model = ProductStore
    extra = 1  # Number of empty ProductStore forms to display

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductStoreInline]

class StoreAdmin(admin.ModelAdmin):
    inlines = [ProductStoreInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ProductStore)
