from django.db import models
from django.db.models import DateField


class Base(models.Model):
    created = DateField(auto_now_add=True)
    updated = DateField(auto_now=True)
