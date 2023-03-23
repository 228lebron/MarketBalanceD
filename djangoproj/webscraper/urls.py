from django.urls import path

from .views import price_difference


urlpatterns = [
    path('price_diff/<str:name>/<str:brand>/', price_difference, name='price_difference'),
]