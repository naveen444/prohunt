from django.db import models
from django.contrib.auth.models import User
from django import template

register = template.Library()

@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value

@register.filter(name='increment_variable')
def increment_variable(value):
    """Allows to update existing variable in template"""
    print(value)
    value =int(value)+1
    print(value)
    input("above line??")
    return value
