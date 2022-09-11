from django import template
from Blog.models import CategoryModel

register = template.Library()

@register.inclusion_tag('folders/category-list.html')
def get_category_list(count=5):
    # the count passed in the functions is the number of categories that should be showed
    latest_categories = CategoryModel.objects.order_by('-created_at')[:count]
    return {'latest_categories':latest_categories}