from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    choices = (('snacks','snacks'),
               ('fast food','fast food'),
               ('food','food'),
               ('ice cream','ice cream'),
               ('juice','juice')
              )

    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100,choices=choices)
    product_desc = models.TextField()
    product_price = models.FloatField()
    product_category = models.TextField()
    product_image = models.ImageField(upload_to='images/')
    product_offer = models.BooleanField(default=False)
    product_like = models.IntegerField(default=0,null=True)
    product_dislike = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    added_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user.username

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    review_time = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pincode = models.IntegerField(null=True)
    city = models.TextField(null=True)
    address = models.TextField(null = True)
    phno = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.user.username






