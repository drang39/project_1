from django.db import models

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


