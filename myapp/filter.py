import django_filters
from django_filters import CharFilter
from .models import *

class UserFilter(django_filters.FilterSet):
    name=CharFilter(field_name='username',lookup_expr='icontains',label='Search     ')
    class Meta:
       model= MyUserData
       fields = ['name']