from django.db import models
from django.contrib.auth.models import User


# Create your models here.

CATEGORY = (

    ('Informatique','Informatique'),
    ('Logistique','Logistique'),
    ('Medical','Medical'),

)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = "CHUM Inventory"

    def __str__(self):
        return f'{self.name} ({self.quantity})'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(User, models.CASCADE, null=True)     
    order_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    date_of_return = models.DateField(null=True, blank=True)  # New field
    returned = models.BooleanField(default=False)  # New field to track return status


    class Meta:
        verbose_name_plural = "Reservations"

    def __str__(self):
        return f'{self.product} ordered by {self.client.username}'
