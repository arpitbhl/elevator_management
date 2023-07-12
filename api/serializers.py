from rest_framework import serializers
from api.models import Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    """
    """
    next_destination = serializers.SerializerMethodField()
    def get_next_destination(self,obj):
        return obj.current_floor

    class Meta:
        model = Elevator
        exclude = ('created_at','updated_at')
    