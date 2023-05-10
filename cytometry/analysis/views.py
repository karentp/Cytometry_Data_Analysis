import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import FileUploadForm


def home(request):
    if request.method == 'POST' and request.FILES.getlist('file'):
        files = request.FILES.getlist('file')
        for file in files:
            if not file.name.endswith('.fcs'):
                return render(request, 'home.html', {'form': FileUploadForm(), 'error': 'Only .fcs files are allowed'})
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            # You can now work with the uploaded file as needed.
            # For example, you could save the filename in a database table for later use.
            # You can access the file with `open(os.path.join(settings.MEDIA_ROOT, filename), 'rb')`

        return render(request, 'home.html', {'form': FileUploadForm(), 'success': 'File(s) uploaded successfully'})
    else:
        form = FileUploadForm()
        return render(request, 'home.html', {'form': form})
