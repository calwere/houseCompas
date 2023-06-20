from django.template import Library

register = Library()

@register.filter
def multiply(value, arg):
    return value * arg
