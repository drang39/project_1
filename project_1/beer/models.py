from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Brand(models.Model):
    brandname = models.CharField(max_length=40,null=False)

    class Meta:
        db_table = "brand"

class Category(models.Model):
    categoryname = models.CharField(max_length=40,null=False)
    categorydescription = models.CharField(max_length=200,null=True)
    class Meta:
        db_table = "category"

class Product(models.Model):
    productname = models.CharField(max_length=40,null=False)
    rating = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=500,null=False)
    productimg = models.CharField(max_length=40,null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)



    class Meta:
        db_table = "product"

class Comment(models.Model):
    rating = models.IntegerField(null=False)
    comment = models.CharField(max_length=200,null=True)
    food = models.CharField(max_length=100,null = True)
    fan = models.IntegerField(null=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "comment"
