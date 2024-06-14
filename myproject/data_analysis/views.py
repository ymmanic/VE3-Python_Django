import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from .utils import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = handle_uploaded_file(file)
            return render(request, 'data_analysis/results.html', data)
    else:
        form = UploadFileForm()
    return render(request, 'data_analysis/upload.html', {'form': form})
