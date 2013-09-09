from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from tcoapp.models import Journey
from tcoapp.serializers import JourneySerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def journeys(request):
    context = {}
    return render(request, 'tcoapp/journeys.html', context)



@csrf_exempt
def journey_list(request):
    """
    List all journeys, or create a new journey.
    """
    if request.method == 'GET':
        journeys = Journey.objects.all()
        serializer = JourneySerializer(journeys, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JourneySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def journey_detail(request, pk):
    """
    Retrieve, update or delete a journey.
    """
    try:
        journey = Journey.objects.get(pk=pk)
    except Journey.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = JourneySerializer(journey)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = JourneySerializer(journey, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        journey.delete()
        return HttpResponse(status=204)
