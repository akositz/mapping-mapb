from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
    context = {
        'test':11}
    rendered_template = render(request, 'mapapp/index.dtl', context)

    return rendered_template

def point_data(request):
    data = {
        "points": [
            [20, 20]
        ]
    }

    return JsonResponse(data)
    
