from django.db import models
from django.contrib.auth.models import User
from django import template

register = template.Library()

@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value
