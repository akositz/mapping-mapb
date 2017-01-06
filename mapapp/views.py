from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'test':11}
    rendered_template = render(request, 'mapapp/index.dtl', context)

    return rendered_template
