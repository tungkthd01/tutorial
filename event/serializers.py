from rest_framework import serializers
from event.models import Events, Drawwings
from event.models import Image_paths,Performances,Tickets
class EventSerializers(serializers.ModelSerializer):

    class Meta:
        model =  Events
        fields = ['event_id','type','title']

class ImagePathApi(serializers.ModelSerializer):

    class Meta:
        model = Image_paths
        fields = '__all__'

class EventListApit(serializers.ModelSerializer):
    title = serializers.CharField(source="event_id.title")
    type = serializers.IntegerField(source="event_id.type")

    class Meta:

        model = Image_paths
        fields = ['event_id','title','image_url','type']

#Validate the presence of access user.
class PerformanceTicket(serializers.ModelSerializer):
    is_archived = serializers.SerializerMethodField()
    ticket_available_flag = serializers.SerializerMethodField()
    class Meta:
        model = Tickets
        fields = ['ticket_id','ticket_available_flag','is_archived','drawing_flag','drawing_application_deadline','drawing_status']
    def get_is_archived(self,obj):
        is_archive = obj.performance_id.event_id.is_archived
        if is_archive is not None:
            return is_archive
        else:
            return 0
    def get_ticket_available_flag(self,obj):
        ticket_available_flag = obj.performance_id.ticket_available_flag
        if ticket_available_flag is not None:
            return ticket_available_flag
        else:
            return  0
"""Generate JSON response.								
	3-1)Mapping"""
class TickePerformancesSerializer(serializers.ModelSerializer):
    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()
    quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Tickets
        fields = ['ticket_id','name','start_datetime','end_datetime','price','quantity','total_price']

    def get_start_datetime(self,obj):
        start_datetime = obj.performance_id.start_datetime
        if start_datetime is not None:
            return start_datetime
        else:
            return  ""
    def get_end_datetime(self,obj):
        end_datetime = obj.performance_id.end_datetime
        if end_datetime is not None:
            return end_datetime
        else:
            return  ""
    def get_quantity(self,obj):
        return 1
    def get_total_price(self,obj):
        total_price = obj.price
        if total_price is not None:
            return total_price
        else:
            return  ""

#2-1)Create drawing record
class DrawingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drawwings
        fields = ['ticket_id','is_elected','is_purchased']

