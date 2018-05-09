from django.db import models


class Product(models.Model):
    product_type_choices = (
        ('BC', 'Bicycle'),
        ('BK', 'Book'),
        ('CD', 'CD'),
    )
    product_type = models.CharField(max_length=2, choices=product_type_choices, default='No Product')
    product_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    product_price = models.FloatField()
    product_specs = models.CharField(max_length=500)
    product_pics = models.FileField(blank=True)
    product_multimedia = models.FileField(blank=True)

    def __str__(self):  # __unicode__ on Python 2 //to make the object string visible when calling it
        return self.product_name


class BuyOrder(models.Model):
    product_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=300)
    zip_code = models.IntegerField()

    def __str__(self):  # __unicode__ on Python 2 //to make the object string visible when calling it
        return self.product_name

