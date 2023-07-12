from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import ElevatorSerializer
from api.models import Elevator

class ElevatorView(APIView):

    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def get(self, request, pk = None, elevator_system  = None):
        try:
            elevator = self.queryset.filter(elevator_system = elevator_system).get(pk = pk)
            context = {}
            serializer = ElevatorSerializer(elevator)
            context["elevator_system"] = elevator_system
            context["data"] = serializer.data
            return Response(context)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk = None, elevator_system = None):
        try:
            elevator = self.queryset.filter(elevator_system = elevator_system).get(pk = pk)
            serializer = ElevatorSerializer(elevator, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
            context = {}
            context["elevator_system"] = elevator_system
            context["data"] = serializer.data
            return Response(context)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    