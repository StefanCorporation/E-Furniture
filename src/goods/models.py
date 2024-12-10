from django.db import models

# Create your models here.


class Categorys(models.Model):
    name = models.CharField(max_length=159, unique=True, blank=True, verbose_name='Name')
    slug = models.SlugField(max_length=239, unique=True, blank=True, null=True, verbose_name='SLUG-URL')


    class Meta:
        db_table = 'category'  
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Products(models.Model):
    name = models.CharField(max_length=159, unique=True, blank=True, verbose_name='Name')
    slug = models.SlugField(max_length=239, unique=True, blank=True, null=True, verbose_name='SLUG-URL')
    description = models.TextField(blank=True, null=True, verbose_name='description')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Images')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Price')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Discount')
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Quantity')
    category = models.ForeignKey(to=Categorys, on_delete=models.CASCADE, verbose_name='Category')


    class Meta:
        db_table = 'product'  
        verbose_name = 'Product'
        verbose_name_plural = 'Products'