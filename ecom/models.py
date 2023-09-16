from django.db import models

class Store(models.Model):
    Products = models.ManyToManyField('Product', related_name='stores', through='ProductStore')
    StoreID = models.AutoField(primary_key=True)
    StoreName = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.StoreName

    class Meta:
        verbose_name_plural = "Stores"


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

    class Meta:
        verbose_name_plural = "Products"

class ProductStore(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.ProductName} at {self.store.StoreName}"
