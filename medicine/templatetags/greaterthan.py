__author__ = 'soheil'
from django import template
register = template.Library()

@register.filter
def gt(a, b):

    return a < b