from django.template import Library

register = Library()

@register.simple_tag()
def review_exists():
    return True