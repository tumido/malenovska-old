from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def split(value, args):
    if args is None:
        value.split(" ")
    args = args.split(",")
    parts = value.split(args[0])
    return parts[int(args[1])]
