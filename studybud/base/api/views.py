from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from django.http import JsonResponse


@api_view(['GET', ])
def get_routes(request):
    routers = [
        'GET /api',
        'GET /api/rooms',
    ]

    return Response(routers)


@api_view(['GET', ])
def get_rooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def get_room(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room)
    return Response(serializer.data)
