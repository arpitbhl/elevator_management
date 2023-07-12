from django.contrib import admin
from .models import Elevator,ElevatorSystem,ElevatorRequests

# Then are the primary keys of the Classes to be shown to the admin only
class ElevatorAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class ElevatorSystemAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class ElevatorRequestsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# This is to add the models in admin section
admin.site.register(Elevator,ElevatorAdmin)
admin.site.register(ElevatorSystem, ElevatorSystemAdmin)
admin.site.register(ElevatorRequests,ElevatorRequestsAdmin)