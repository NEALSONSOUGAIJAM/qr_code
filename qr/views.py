from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings


def generate_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR code
            qr = qrcode.make(url)
            file_name = res.replace(" ", "_").lower() + "_menu.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)  # ../media/restaurant_menu.png
            qr.save(file_path)

            # Create image URL
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            context = {
                'res': res,
                'qr_url': qr_url,
                'file_name': file_name
            }
            return render(request, 'qr_result.html', context)
    else:
        form = QRCodeForm()  # Initialize a blank form for GET requests

    # Render the form if the method is GET or the form is invalid
    context = {
        'form': form,
    }
    return render(request, 'generate_code.html', context)
