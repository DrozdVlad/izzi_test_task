from datetime import datetime

from django.db import models


class Order(models.Model):
    """ From the order there should be a link to the product(I think it will be ManyToManyField),
     which should also have certain fields,but for simplicity of the project, I left it as it is. """

    date_of_create = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=30)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)
    date_of_registration = models.DateField(default=datetime.now)
    order = models.OneToOneField(Order, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
