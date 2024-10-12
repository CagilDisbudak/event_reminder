import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from .models import Event
from .serializers import EventSerializer

logger = logging.getLogger('api')

@api_view(['GET', 'POST'])
def event_list_create_view(request):
    if request.method == 'GET':
        logger.info("GET /events/ - Retrieving all events")
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        logger.debug(f"Retrieved {len(events)} events")
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        logger.info("POST /events/ - Creating a new event")
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Event created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Failed to create event: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail_view(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        logger.warning(f"Event with id {pk} does not exist")
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        logger.info(f"GET /events/{pk}/ - Retrieving event")
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        logger.info(f"PUT /events/{pk}/ - Updating event")
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Event with id {pk} updated successfully")
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            logger.error(f"Failed to update event: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        logger.info(f"DELETE /events/{pk}/ - Deleting event")
        event.delete()
        logger.info(f"Event with id {pk} deleted successfully")
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def upcoming_events_view(request):
    now = timezone.now()
    next_24_hours = now + timedelta(hours=24)
    logger.info("GET /events/upcoming - Retrieving upcoming events")
    events = Event.objects.filter(date__gte=now, date__lte=next_24_hours)
    serializer = EventSerializer(events, many=True)
    logger.debug(f"Retrieved {len(events)} upcoming events")
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def events_by_category_view(request, categoryName):
    logger.info(f"GET /events/category/{categoryName}/ - Retrieving events by category")
    events = Event.objects.filter(category=categoryName)
    serializer = EventSerializer(events, many=True)
    logger.debug(f"Retrieved {len(events)} events in category {categoryName}")
    return Response(serializer.data, status=status.HTTP_200_OK)
