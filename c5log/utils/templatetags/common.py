from django import template
from django.core.paginator import EmptyPage, PageNotAnInteger


register = template.Library()

@register.filter
def colorize(value):
	"""
	This genious filter was taken from Bernhard Essl's django-irc-logs 
	project at https://github.com/bessl/django-irc-logs.com.
	"""
	if not value:
		return ""
	color = sum([ord(c) for c in value])
	return "#%X" % color


#  Based on: http://www.tummy.com/articles/django-pagination/
@register.inclusion_tag('bootstrap_paginator.html', takes_context=True)
def paginator(context, adjacent_pages=2):
    page_num = int(context['page'])
    paginator = context['paginator']
    try:
        page_object = paginator.page(page_num)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)

    startPage = max(page_num - adjacent_pages, 1)
    if startPage <= 3: startPage = 1

    endPage = page_num + adjacent_pages + 1

    if endPage >= paginator.num_pages - 1: endPage = paginator.num_pages + 1

    page_numbers = [n for n in range(startPage, endPage) \
            if n > 0 and n <= paginator.num_pages]

    return {
        'page_obj': page_object,
        'paginator': paginator,
        'results_per_page': paginator.per_page,
        'page': page_num,
        'pages': paginator.num_pages,
        'page_numbers': page_numbers,
        'next': page_object.next_page_number,
        'previous': page_object.previous_page_number,
        'has_next': page_object.has_next,
        'has_previous': page_object.has_previous,
        'show_first': 1 not in page_numbers,
        'show_last': paginator.num_pages not in page_numbers,
        'url_name': context['request'].resolver_match.url_name,
        'query_strings': context['request'].GET.urlencode()
    }