from django import template
from Blog.models import *

register = template.Library()

@register.inclusion_tag('folders/category-list.html')
def get_category_list():
    return {'cats': CategoryModel.objects.all()}