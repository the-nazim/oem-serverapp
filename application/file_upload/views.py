from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Files
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponseNotFound, JsonResponse
# Create your views here.


def upload_file(request):
    if request.method=='POST':
        file = request.FILES['file']
        description = request.POST.get('description')
        file_name = file.name
        file_obj = Files(
            file_name = file_name,
            file = file,
            description = description if description else None
        )
        file_obj.save()

        messages.success(request, f"File {file.name} uploaded successfully!")
        return redirect('send_file', file_id=file_obj.id)
    return render(request, 'upload_file.html')

def list_file(request):
    file_data = Files.objects.all()
    
    return render(request, "list_file.html", {'files':file_data})

def send_file(request, file_id):
    file_instance = get_object_or_404(Files, id=file_id)
    file_path = file_instance.file.path
    try:
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_instance.file_name)
        return response
    except FileNotFoundError as e:
        print("Error ", e)
        return HttpResponseNotFound("The requested file does not exist")

def latest_file(request):
    latest_file = Files.objects.latest('datetime')

    return JsonResponse({
        'latest_datetime':latest_file.datetime.isoformat(),
        'file_name':latest_file.file_name,
        'file_id':latest_file.id
    })