import django_filters
from .models import Blog


class BlogFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__en_name', lookup_expr='exact')

    class Meta:
        model = Blog
        fields = ["category"]
