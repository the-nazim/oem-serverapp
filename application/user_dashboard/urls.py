from django.urls import path
from . import views
# from .admin import CustomAdminSite
from .models import Client, Vehicle_detail

urlpatterns = [
    path('dashboard/', views.user_home, name="dashboard"),
    # path('admin/dashboard/', views.admin_dashboard, name="admin_dashboard"),
]

# custom_admin_site = CustomAdminSite()

# # Register your models with the custom admin site
# custom_admin_site.register(Client)
# custom_admin_site.register(Vehicle_detail)

# urlpatterns = [
#     path('admin/', custom_admin_site.urls),
# ]