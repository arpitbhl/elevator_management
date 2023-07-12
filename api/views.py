from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import ElevatorSerializer,ElevatorSystemSerializer,ElevatorRequestsSerializer,ElevatorSystemOnlySerializer
from api.models import Elevator,ElevatorSystem,ElevatorRequests

class RoutesView(APIView):

    
    routes = [
        'GET /',
        'GET /system/',
        'GET /system/<int:elevator_system_id/<int:pk/',
        'GET /elevators/',
        'GET /elevators/<int:elevator_system_id>/<int:pk>/',
        'GET /requests/',
        'GET /requests/<int:elevator_system_id>/<int:pk>/',

    ]
    def get(self,request):
        return Response(self.routes)
    

class ElevatorView(APIView):

    
    serializer_class = ElevatorSerializer

    def get(self,request):
        try:
            
            elevator = Elevator.objects.all()
            serializer = ElevatorSerializer(elevator,many = True)
            context = serializer.data
            return Response(context)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
class ElevatorViewByPk(APIView):

    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def get(self,request,elevator_system =None, pk=None):
        try:
            
            elevator = self.queryset.filter(elevator_system = elevator_system).get(pk = pk)
            context = {}
            serializer = ElevatorSerializer(elevator)
            context["elevator_system"] = elevator_system
            context["data"] = serializer.data

            return Response(context)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,elevator_system = None, pk = None):
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

class ElevatorSystemView(APIView):

    
    serializer_class = ElevatorSystemOnlySerializer
    
    def get(self, request):
        
        try:
            elevator_system = ElevatorSystem.objects.all()
            serializer = ElevatorSystemOnlySerializer(elevator_system,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Elevator s System doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
    
    
class ElevatorSystemViewByPk(APIView):

    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

    def get(self, request, system_name = None):
        try:
            elevator_system = self.queryset.filter(system_name = system_name)
            serializer = ElevatorSystemSerializer(elevator_system)
            print(serializer.data,serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Elevator System doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, system_name = None):
        try:
            elevator_system = self.get_object()
            serializer = ElevatorRequestsSerializer(data = request.data)
            req_floor = serializer.initial_data['req_floor']
            to_floor = serializer.initial_data['to_floor']
            
            # Query to get closest elevator 
            closest_elevator = Elevator.objects.filter(elevator_system = elevator_system, is_operational = True).annotate(distance = Func(F('current_floor')-req_floor,function = 'ABS')).order_by('distance').first()
            # If closest elevator is available
            if closest_elevator is not None:
                direction = (to_floor - req_floor) / abs(to_floor - req_floor)
                closest_elevator.direction = direction
                closest_elevator.current_floor = to_floor
                closest_elevator.save()
                serializer.initial_data['elevator'] = closest_elevator.id
                if serializer.is_valid():
                    elevator_request = serializer.save()
                    context = ElevatorRequestsSerializer(elevator_request).data
                    return Response(context)
        except Exception as e:
            return Response({'error': "Elevator System not found"}, status=status.HTTP_404_NOT_FOUND)

class ElevatorRequestsView(APIView):

    queryset = ElevatorRequests.objects.all()
    serializer_class = ElevatorRequestsSerializer

    def get(self, request):
        try:
            elevator = Elevator.objects.all()
            request = ElevatorRequests.objects.all()
            serializer = ElevatorRequestsSerializer(request, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Elevator doesn't Exist"}, status=status.HTTP_404_NOT_FOUND)
    


class ElevatorRequestsViewByPk(APIView):

    queryset = ElevatorRequests.objects.all()
    serializer_class = ElevatorRequestsSerializer

    def get(self, request, elevator_system  = None,  pk = None):
        try:
            elevator = Elevator.objects.filter(elevator_system = elevator_system).get(pk = pk)
            request = ElevatorRequests.objects.filter(elevator = elevator)
            serializer = ElevatorRequestsSerializer(request, many = True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': "Elevator doesn't Exist"}, status=status.HTTP_404_NOT_FOUND)