import io
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from matplotlib import pyplot as plt

from .models import UploadedFile
from .forms import FileUploadForm
import flowkit

def home(request):
    if request.method == 'POST' and request.FILES.getlist('file'):
        files = request.FILES.getlist('file')
        for file in files:
            if not file.name.endswith('.fcs'):
                return render(request, 'home.html', {'form': FileUploadForm(), 'error': 'Only .fcs files are allowed'})
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            print("filename: ", file, " filepath: ", filename)
            uploaded_file = UploadedFile.objects.create(file=file, file_path=filename)

        request.session['file_path'] = uploaded_file.file_path
        return render(request, 'home.html', {'form': FileUploadForm(), 'success': 'File(s) uploaded successfully'})
    else:
        form = FileUploadForm()
        return render(request, 'home.html', {'form': form})

def plot_1(request):
    # get the uploaded file from the session
    file_id = request.session.get('file_id')
    uploaded_file = UploadedFile.objects.get(id=file_id)
    file_path = uploaded_file.file.path

    # load the flow data from the uploaded file
    sample = flowkit.Sample(file_path)
    data = sample.events

    # get the data for the desired channel
    channel_name = 'FSC-A'
    data = data[channel_name]

    # create the histogram plot
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, bins=100)
    ax.set_xlabel(channel_name)
    ax.set_ylabel('Frequency')

    # convert the plot to a PNG image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # return the image data as an HTTP response
    return HttpResponse(buffer.getvalue(), content_type='image/png')