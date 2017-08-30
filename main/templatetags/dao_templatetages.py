from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.simple_tag
def render_paginator_btn(articles,page):
    current_page = articles.number
    if abs(current_page - page) <= 3 : #display button
        # ele = '''<li><a href="?page={page}&service_name={{ i }}">{page}</a></li>'''.format(page=page)
        ele = '''<li>{page}</li>'''.format(page=page)
        return mark_safe(ele)
    return ''
