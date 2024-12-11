from django.urls import path
from . import views

urlpatterns = [
    path("file/", views.upload_file, name="upload"),
    path("list/", views.list_file, name="list"),
    path("send-file/<int:file_id>/", views.send_file, name="send_file"),
    path("latest-file/", views.latest_file, name='latest_file')
]