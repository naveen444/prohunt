from django.db import models
from django.contrib.auth.models import User
from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''


@register.filter(expects_localtime=True, is_safe=False)
def time(value, arg=None):
    """Format a time according to the given format."""
    if value in (None, ''):
        return ''
    try:
        return formats.time_format(value, arg)
    except (AttributeError, TypeError):
        try:
            return time_format(value, arg)
        except (AttributeError, TypeError):
            return ''

@register.filter(name='max_lst')
def max_lst(products):
    nlst = products.all().order_by('-votes_total')[:3]
    return nlst
