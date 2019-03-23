from django.forms import ModelForm

from weight.models import Weight


class WeightForm(ModelForm):
    class Meta:
        model = Weight
        fields = ['date', 'old_weight', 'new_weight']
