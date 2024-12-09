from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    product_description = models.TextField() 

    def __str__(self):
        return self.product_name

    
