from django import template

register = template.Library()


@register.filter
def empty_stars(value):
    stars = value
    other_stars = 5 - stars
    return other_stars