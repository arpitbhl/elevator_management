from django.db import models


class ElevatorSystem(models.Model):
    """
    
    """
    system_name = models.CharField(max_length=100)
    no_of_floor = models.IntegerField(default=1)
    no_of_elevators = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    
    def _str_(self):
        return self.system_name
    

class Elevator(models.Model):
    """
    """

    direction_choices =(('Upward', 'Upward'), ('Downward', 'Downward'), ('STANDING STILL', 'STANDING STILL'))
    door_choices =(('CLOSE', 'CLOSE'), ('OPEN', 'OPEN'))
    
    
    elevator_system = models.ForeignKey('ElevatorSystem',on_delete=models.CASCADE)
    elevator_id = models.IntegerField()
    current_floor = models.IntegerField(default=1)
    is_operational = models.BooleanField(default = True) # True means its operating otherwise not
    direction = models.CharField(choices=direction_choices,default='STANDING STILL',max_length=20)
    door_status = models.CharField(choices=door_choices,default='OPEN',max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def _str_(self):
        return str(self.elevator_id)
    

class ElevatorRequests(models.Model):
    """
    """
    elevator = models.ForeignKey('Elevator',on_delete=models.CASCADE)
    req_floor = models.IntegerField()
    to_floor = models.IntegerField()
    is_serviced = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    updated_at = models.DateTimeField(auto_now=True,editable=False)

    def _str_(self):
        return str(self.elevator) + " is requested from " + str(self.req_floor) + " floor"