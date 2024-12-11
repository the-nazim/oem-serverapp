from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Client, Vehicle_detail
# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'vehicle_sign')
    search_fields = ('first_name', 'last_name', 'email_address', 'vehicle_sign')
    list_filter = ('first_name', 'last_name')

# Register the Vehicle_details model
class VehicleDetailsAdmin(admin.ModelAdmin):
    list_display = ('model_no', 'chasis_no', 'vehicle_type', 'vehicle_sign', 'mfg_date')
    search_fields = ('model_no', 'chasis_no', 'vehicle_type', 'vehicle_sign')
    list_filter = ('vehicle_type', 'mfg_date')

admin.site.register(Client, ClientsAdmin)
admin.site.register(Vehicle_detail, VehicleDetailsAdmin)

# class CustomAdminSite(AdminSite):
#     site_header = "Admin Dashboard"
#     site_title = "Admin Portal"
#     index_title = "Welcome to the Admin Dashboard"

#     def index(self, request, extra_context=None):
#         # Add custom data for the dashboard
#         user_count = Client.objects.count()
#         vehicle_count = Vehicle_detail.objects.count()
#         vehicle_count_per_user = [Client.objects.filter(vehicle_sign=v.vehicle_sign).count() for v in Vehicle_details.objects.all()]

#         extra_context = extra_context or {}
#         extra_context.update({
#             'user_count': user_count,
#             'vehicle_count': vehicle_count,
#             'vehicle_count_per_user': vehicle_count_per_user,
#         })

#         return super().index(request, extra_context=extra_context)
