from django import template

register = template.Library()

# Custom filter to convert numbers to binary
@register.filter
def convert(value):
    return bin(value)  # Convert the number to binary
    
@register.filter
def int_to_str(x):
    return str(x)