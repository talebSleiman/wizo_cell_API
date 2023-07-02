from django.db import models

# Create your models here.

class Product(models.Model):
    SERVICE_TYPE = (
        ('Alfa','Alfa'),
        ('Touch','Touch')
    )
    CATEGORY_TYPE = (
        ('Recharge Card','Recharge Card'),
        ('Recharge Day','Recharge Day'),
        ('Alfa Gift','Alfa Gift'),
        ('Weekly Data','Weekly Data'),
        ('Alfa Ushare','Alfa Ushare')
    )

    name = models.CharField(max_length=100, verbose_name='Name')
    price = models.FloatField(verbose_name='Price')
    type = models.CharField(max_length=10,choices=SERVICE_TYPE, verbose_name='Service Type')
    category = models.CharField(max_length=20, verbose_name='Category', choices=CATEGORY_TYPE)
    # image = models.ImageField(upload_to='static', verbose_name='Image')
    image = models.CharField(max_length=50,verbose_name='Image Path')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = 'Product'