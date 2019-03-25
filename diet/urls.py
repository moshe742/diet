"""diet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from diet import settings
from weight.views import WeightView, WeightCreate, WeightUpdate, WeightDataView, WeightDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weights/', WeightView.as_view(), name='weight_list'),
    path('get_weights/', WeightDataView.as_view(), name='weight_graph'),
    path('weights/form/<int:pk>/', WeightUpdate.as_view(), name='weight_update'),
    path('weights/form/', WeightCreate.as_view(), name='weight_add'),
    path('weights/delete/<int:pk>/', WeightDelete.as_view(), name='weight_delete'),
] + static(settings.STATIC_ROOT)
