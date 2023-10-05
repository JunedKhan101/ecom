from django.contrib import admin
from .models import Product, Store, Category, CategoryAndProduct, CategoryAndStore

# Define the inline classes
class CategoryAndProductInline(admin.TabularInline):
    model = CategoryAndProduct
    extra = 1  # Number of empty CategoryAndProduct forms to display

class CategoryAndStoreInline(admin.TabularInline):
    model = CategoryAndStore
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [CategoryAndProductInline]
    list_display = ('ProductName', 'display_stores', 'display_categories')

    def display_stores(self, obj):
        # Retrieve the associated stores for the product
        stores = Store.objects.filter(Categories__Products=obj)
        return ", ".join([store.StoreName for store in stores])

    def display_categories(self, obj):
        # Retrieve the associated categories for the product
        categories = Category.objects.filter(Products=obj)
        return ", ".join([category.CategoryName for category in categories])

    # Set a custom column header
    display_stores.short_description = 'Stores'
    display_categories.short_description = 'Categories'

class StoreAdmin(admin.ModelAdmin):
    inlines = [CategoryAndStoreInline]

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryAndStoreInline, CategoryAndProductInline]
    list_display = ('CategoryName', 'display_stores')

    def display_stores(self, obj):
        # Retrieve the associated stores for the category
        stores = CategoryAndStore.objects.filter(category=obj)
        return ", ".join([store.store.StoreName for store in stores])

    display_stores.short_description = 'Stores'  # Set a custom column header

# Register the models with the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(CategoryAndProduct)
# admin.site.register(CategoryAndStore)
