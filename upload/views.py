from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'upload_form.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()   
        return render(request, 'upload_form.html', {'form': form})
    
def show_images(request):
    if request.method=='GET':
        images=Image.objects.all()
        return render(request, 'index.html', {'images': images})
