from django import template

register = template.Library()

@register.filter
def mediapath(image_path):
    if image_path:
        return f"/media/{image_path}"
    else:
        return ""