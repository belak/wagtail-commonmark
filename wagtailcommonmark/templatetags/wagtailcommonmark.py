from django import template

from ..utils import render_commonmark

register = template.Library()


@register.filter(name='commonmark')
def commonmark(value):
    return render_commonmark(value)
