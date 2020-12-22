import django_filters
from django_filters import DateFilter , CharFilter
from .models import Order ,Customer , Product

class OrderFillter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date_created" , lookup_expr = 'gte')
    end_date = DateFilter(field_name = "date_created" , lookup_expr = 'lte')
    Note = CharFilter(field_name = "Note" , lookup_expr = 'icontains')


    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer' ,  'date_created']