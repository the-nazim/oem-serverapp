from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Client, Vehicle_detail

# Dashboard View with Static Data
def user_home(request):

    user_count = Client.objects.count()  #10 
    vehicle_count = Vehicle_detail.objects.count()  #25  

    vehicle_count_per_user = []
        #client.vehicles.count() for client in Client.objects.all()
    
    #[3, 5, 1, 2, 4, 1, 3, 2, 3, 4]  # Number of vehicles per user

    for client in Client.objects.all():
        count = Vehicle_detail.objects.filter(vehicle_sign=client.vehicle_sign).count()
        vehicle_count_per_user.append(count)

    context = {
        'user_count': user_count,
        'vehicle_count': vehicle_count,
        'vehicle_count_per_user': vehicle_count_per_user,
    }

    return render(request, 'dashboard.html', context)


# @staff_member_required  # Ensures only admin users can access
# def admin_dashboard(request):
#     # Static data (replace with dynamic queries if needed)
#     user_count = 10  # Example count
#     vehicle_count = 25
#     vehicle_count_per_user = [3, 5, 1, 2, 4, 1, 3, 2, 3, 4]

#     context = {
#         'user_count': user_count,
#         'vehicle_count': vehicle_count,
#         'vehicle_count_per_user': vehicle_count_per_user,
#     }
#     return render(request, 'admin01/dashboard.html', context)
