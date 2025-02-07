from datetime import date

from django.db import models
from django.db.models import DateField, DecimalField
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.


class Base(models.Model):
    created = DateField(auto_now_add=True)
    updated = DateField(auto_now=True)

    class Meta:
        abstract = True


class Weight(Base):
    date = DateField(default=now)
    old_weight = DecimalField(max_digits=4, decimal_places=1)
    new_weight = DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f'{str(self.date)}- {str(self.old_weight)} - {str(self.new_weight)}'

    def get_absolute_url(self):
        return reverse('weight_list')
