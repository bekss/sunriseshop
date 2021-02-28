from django import template
from ..models import Tovar, Category

register = template.Library()

@register.inclusion_tag('menu.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories':categories}

