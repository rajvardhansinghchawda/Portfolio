from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg  # Correctly multiplies proficiency by 20 for %