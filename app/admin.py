from django.contrib import admin
from .models import UserProfile,Add_Vehicle

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','cleremont_id','first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']

class AddVehicleAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle_name',
        'celermont_id',
        'groups',
        'zones',
        'current_speed',
        'max_speed',
        'average_speed',
        'distance',
        'battery',
        'can_grab_marketplace_jobs',
        'gps',
        'current_location',
        'heading_to',
        'last_connected',
        'last_tracked',
        'connection',
        'checked_in_at',
        'map',
        'action',
    )

    search_fields = ('vehicle_name', 'celermont_id', 'groups')  # Add any fields you want to be searchable

admin.site.register(Add_Vehicle, AddVehicleAdmin)

