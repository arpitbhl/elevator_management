from django.db import models


class ElevatorSystem(models.Model):
    """
    
    """
    system_name = models.CharField(max_length=100)
    no_of_floor = models.IntegerField(default=1)
    no_of_elevators = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    
    def __str__(self):
        return self.system_name
    

class Elevator(models.Model):
    """
    """

    direction_choices =((1, 'UP'), (-1, 'DOWN'), (0, 'STANDING STILL'))
    door_choices =((1, 'CLOSE'), (0, 'OPEN'))
    
    
    elevator_system = models.ForeignKey('ElevatorSystem',on_delete=models.CASCADE)
    elevator_id = models.IntegerField()
    current_floor = models.IntegerField(default=1)
    is_operational = models.BooleanField(default = True) # True means its operating otherwise not
    direction = models.CharField(choices=direction_choices,default=0,max_length=1)
    door_status = models.CharField(choices=door_choices,default=0,max_length=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.elevator_id
    

# class ElevatorRequests(models.Model):
#     """
#     """
#     elevator = models.ForeignKey('Elevator',on_delete=models.CASCADE)
    
#     created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
#     updated_at = models.DateTimeField(auto_now=True,editable=False)