from rest_framework import serializers
from api.models import Elevator,ElevatorSystem,ElevatorRequests

class ElevatorSerializer(serializers.ModelSerializer):
    next_destination = serializers.SerializerMethodField()
    def get_next_destination(self,obj):
        return obj.current_floor

    class Meta:
        model = Elevator
        exclude = ('created_at','updated_at')

class ElevatorSystemOnlySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ElevatorSystem
        exclude = ('created_at','updated_at')

class ElevatorSystemSerializer(serializers.ModelSerializer):
    
    elevators = serializers.SerializerMethodField()
    
    class Meta:
        model = ElevatorSystem
        exclude = ('created_at','updated_at')
    
    def get_all_elevators(self,obj):
        elevators = Elevator.objects.filter(elevator_system = obj)
        return ElevatorSerializer(elevators,many = True).data
    
    
    def create_elevator(self,validated_data):
        elevator_system = ElevatorSystem.objects.create(**validated_data)
        no_of_elevators = validated_data.get('no_of_elevators')
        if no_of_elevators is not None:
            for elevator_id in range(1,no_of_elevators + 1):
                Elevator.objects.create(elevator_system = elevator_system,elevator_id = elevator_id)
        return elevator_system


class ElevatorRequestsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ElevatorRequests
        fields = ['id','elevator', 'req_floor', 'to_floor', 'is_serviced']