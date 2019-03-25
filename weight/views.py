import logging

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from weight.forms import WeightForm
from weight.models import Weight

logger = logging.getLogger(__name__)


# @method_decorator(login_required, name='dispatch')
class WeightView(ListView):
    model = Weight
    template_name = 'weight/weight_list.html'
    context_object_name = 'weights'
    ordering = '-date'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = WeightForm()
        return context


class WeightDataView(View):
    def get(self, request):
        weights = Weight.objects.order_by('date').all()
        dates = []
        old_weights = []
        new_weights = []
        for item in weights:
            dates.append(item.date.isoformat())
            old_weights.append(item.old_weight)
            new_weights.append(item.new_weight)

        old_weight = {
            'x': dates,
            'y': old_weights,
            'mode': 'lines+markers',
            'name': 'old weight'
        }
        new_weight = {
            'x': dates,
            'y': new_weights,
            'mode': 'lines+markers',
            'name': 'new weight'
        }

        return JsonResponse({
            'old_weight': old_weight,
            'new_weight': new_weight,
        })


class WeightCreate(CreateView):
    model = Weight
    fields = ['date', 'old_weight', 'new_weight']


class WeightUpdate(UpdateView):
    model = Weight
    fields = ['date', 'old_weight', 'new_weight']


class WeightDelete(DeleteView):
    model = Weight
    context_object_name = 'weight'
    success_url = reverse_lazy('weight_list')
