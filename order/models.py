from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    order_user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_total = models.FloatField()
    order_status = models.CharField(
        default='P',
        max_length=1,
        choices=(
            ('P', 'Pending'),
            ('A', 'Approved'),
            ('R', 'Reproved'),
            ('S', 'Sent'),
            ('D', 'Delivered'),
        )
    )

    def __str__(self):
        return f'Order Nº {self.pk}'


class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    product_id = models.PositiveIntegerField()
    variety = models.CharField(max_length=50)
    variety_id = models.PositiveIntegerField()
    price = models.FloatField()
    price_sale = models.FloatField(default=0)
    quantity = models.PositiveIntegerField()
    image = models.CharField(max_length=1000)

    def __str__(self):
        return f'Item from {self.order}'
