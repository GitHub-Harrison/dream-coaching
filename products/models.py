from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.DurationField()

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """
    model for registered users to leave a review
    """
    product = models.ForeignKey(
        Product, related_name='reviews', null=True,
        blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
