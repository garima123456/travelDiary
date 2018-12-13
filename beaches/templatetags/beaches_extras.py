from django import template
from beaches.models import Category

register = template.Library()

@register.inclusion_tag('beaches/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}
