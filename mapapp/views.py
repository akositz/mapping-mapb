from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from mapapp.forms import PointsForm


def index(request):
    print("=====================================")
    print(request)
    print(dir(request))
    print(request.method)
    print("=====================================")
    points_form = PointsForm()

    if request.method == "POST":
        print("into the database")
        submit_form = PointsForm(request.POST)

        if submit_form.is_valid():
            submit_form.save()

    context = {
        'test': 11,
        'form': points_form
    }
    rendered_template = render(request, 'mapapp/index.dtl', context)

    return rendered_template

def point_data(request):
    data = {
        "points": [
            [13.5, 53.5]
        ]
    }

    return JsonResponse(data)
    
