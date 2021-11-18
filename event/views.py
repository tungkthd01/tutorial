from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from event.models import Events,Tickets,Performances
from event.serializers import EventSerializers, EventListApit, PerformanceTicket, DrawingSerializer, \
    TickePerformancesSerializer
from event.models import Image_paths
from rest_framework import viewsets,generics,permissions,status
from event.paginator import EventPagination
from django.http import Http404
# Create your views here.
class EventsViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Events.objects.filter(is_archived = 0)
    serializer_class = EventSerializers
    pagination_class = EventPagination

    # def get_permissions(self):
    #     if self.action in ['retrieve','list']:
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]

    def get_queryset(self):
        events = Events.objects.filter(is_archived = 1)
        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            events = events.filter(title__icontains=keyword)
        type_event = self.request.query_params.get('type')

        if type_event is not None:
            if type_event == '1' or type_event == '2' :
                events = events.filter(type=type_event)
            elif type_event == 'unspecified':
                events = events.filter(type__in = ['1','2'])
        return events

class EventListView(APIView):
    queryset = Events.objects.filter(is_archived=0)
    serializer_class = EventListApit

    def get(self, request, format=None):
        events = Events.objects.filter(is_archived=0)
        keyword = self.request.query_params.get('keyword')
        eventview = []
        if keyword is not None:
            events = events.filter(title__icontains=keyword)

        type_event = self.request.query_params.get('type')
        if type_event is not None:
            print(type_event)
            if type_event == '1' or type_event == '2':
                event = events.filter(type = (type_event))
                for e in event:
                    id = e.event_id
                    image = Image_paths.objects.filter(event_id=id)
                    serializer_class1 = EventListApit(image, many=True)
                    eventview.append(serializer_class1.data)
            # serializer_class = EventSerializers(event,many=True)
            # #serializer_class1 = EventListApit(image, many=True)
            elif type_event == 'unspecified':
                events = events.filter(type__in = ['1','2'])
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(eventview,status=status.HTTP_200_OK)
# /api/v1/ticket
class TicketPerformance(APIView):
    #ticket = Tickets.objects.prefetch_related('performance','events').all()
    def get(self, request, format=None):
        ticket = Tickets.objects.all()
        serializer = PerformanceTicket(ticket, many=True)
        return Response(serializer.data)
    # def get(self,request):
    # #return Response(status=status.HTTP_200_OK)

class TicketPerformanceDetail(APIView):
    def get_object(self, pk):
        try:
            return Tickets.objects.get(pk=pk)
        except Tickets.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        print(snippet)
        serializer = PerformanceTicket(snippet)

        return Response(serializer.data)


class DrawingsCreat(APIView):
    def get_object(self, pk):
        try:
            return Tickets.objects.get(pk=pk)
        except Tickets.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PerformanceTicket(snippet)
        id_ticket = serializer.data['ticket_id']
        data = {'ticket_id': id_ticket,
                'is_elected': 0,
                'is_purchased':0}
        serializer2 =TickePerformancesSerializer(snippet)
        serializer1 = DrawingSerializer( data=data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer2.data)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)