from django.shortcuts import render
from django.db.models import Count
from .models import Client, Vehicle_detail

# Dashboard View with Updated Data
def user_home(request):

    user_count = Client.objects.count()  # Total number of users
    vehicle_count = Vehicle_detail.objects.count()  # Total number of vehicles

    same_person_multiple_vehicles_data = (
        Client.objects
        .values('first_name', 'last_name')
        .annotate(vehicle_count=Count('vehicle_sign', distinct=True))
        .filter(vehicle_count__gt=1)  # Filter only clients with more than 1 vehicle
    )

    # Collect data for the graph
    client_names = [f"{item['first_name']} {item['last_name']}" for item in same_person_multiple_vehicles_data]
    vehicle_counts = [item['vehicle_count'] for item in same_person_multiple_vehicles_data]

    # Aggregate vehicle type counts
    vehicle_type_data = (
        Vehicle_detail.objects
        .values('vehicle_type')
        .annotate(count=Count('id'))
    )
    vehicle_type_labels = [item['vehicle_type'] for item in vehicle_type_data]
    vehicle_type_counts = [item['count'] for item in vehicle_type_data]

    context = {
        'user_count': user_count,
        'vehicle_count': vehicle_count,
        'client_names': client_names,  # Names for the graph's X-axis
        'vehicle_counts': vehicle_counts,  # Number of vehicles for Y-axis
        'vehicle_type_labels': vehicle_type_labels,  # Vehicle types for second graph
        'vehicle_type_counts': vehicle_type_counts,  # Counts for second graph
    }

    return render(request, 'dashboard.html', context)