from datetime import date
from django.db.models import DateField, DecimalField, CharField

from eating import Base
# Create your models here.


class Intake(Base):
    date = DateField(default=date.today())
    breakfast = CharField()
