from django.db import models
from django.utils.text import slugify

class Store(models.Model):
    Categories = models.ManyToManyField('Category', related_name='categories', through='Linker')
    StoreID = models.AutoField(primary_key=True)
    StoreName = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.StoreName

    class Meta:
        verbose_name_plural = "Stores"

class Category(models.Model):
    Products = models.ManyToManyField('Product', related_name='categories', through='Linker')
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=30, default="")
    slug = models.SlugField(unique=True, default='')

    def __str__(self):
        return self.CategoryName

    def display_stores(self, obj):
        # Create a string with the names of associated stores
        stores = obj.stores.all()
        return ", ".join([store.StoreName for store in stores])

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=30, default="")
    ProductDescription = models.CharField(max_length=100, default="")
    slug = models.SlugField(unique=True, default='')
    Image = models.ImageField(upload_to="uploads", null=True, blank=True, default="")
    ListPrice = models.DecimalField(max_digits=6, decimal_places=2)
    SalesPrice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.ProductName
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ProductName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Products"
    
class CategoryAndProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.ProductName} at {self.category.CategoryName}"
    
class CategoryAndStore(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store.StoreName} at {self.category.CategoryName}"

class Linker(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.ProductName} at {self.category.CategoryName}"
