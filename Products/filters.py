import django_filters
from .models import Mobile,Product

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='discount_price', lookup_expr='gt')
    price_max = django_filters.NumberFilter(field_name='discount_price', lookup_expr='lt')
    brand = django_filters.CharFilter(field_name='brand', lookup_expr='icontains')
    is_trending = django_filters.BooleanFilter(field_name='trending')

    class Meta:
        model = Mobile
        fields = ['price_min', 'price_max', 'brand', 'is_trending']