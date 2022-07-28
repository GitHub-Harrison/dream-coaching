import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ generate a random unique order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        update grand total each time a new item
        is added to the bag/cart
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        override the original save method to set
        order number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)
    date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        override the original save method to set the lineitem total
        and update the order total
        """
        self.lineitem_total = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
