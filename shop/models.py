from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Order(models.Model):
    item=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=20)
    address=models.CharField(max_length=300)
    land=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=10)
    emergency=models.CharField(max_length=10,null=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=20)
    zip=models.CharField(max_length=10)
    total=models.CharField(max_length=15)

    def __str__(self):
        return self.email