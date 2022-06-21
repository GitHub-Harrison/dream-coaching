from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Package(models.Model):

    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tier = models.BooleanField(default=False, null=True, blank=True)
    sku = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.DurationField()
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name
