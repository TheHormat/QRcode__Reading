from django.shortcuts import render, redirect
from .models import QrCode
# Create your views here.


def home(request):
    qr_codes = QrCode.objects.all()
    for qr in qr_codes:
        qr.qr_image_path = f"qr_codes/{qr.id}.png"
    context = {"qr_codes": qr_codes}
    return render(request, "index.html", context)


def qr_redirect(request, qr_id):
    qr_code = QrCode.objects.get(id=qr_id)
    qr_code.scan_count += 1
    qr_code.save()
    return redirect(qr_code.url)

