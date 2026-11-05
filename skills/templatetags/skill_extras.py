from django import template

register = template.Library()


@register.filter
def duration_label(weeks):
    try:
        weeks = int(weeks)
    except (TypeError, ValueError):
        return ""
    return f"{weeks} week{'s' if weeks != 1 else ''}"
