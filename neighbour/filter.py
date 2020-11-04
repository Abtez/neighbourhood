import django_filters
from .models import *

class PostFilter(djanfo_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['username' ]