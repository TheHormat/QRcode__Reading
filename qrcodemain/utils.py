import qrcode

def create_qr_code_image(url, qr_id):
    url = f"http://192.168.0.104:8000/qr/{qr_id}/"
    qr_image = qrcode.make(url)
    qr_image_path = f"static/qr_codes/{qr_id}.png"
    qr_image.save(qr_image_path)
    return qr_image_path  # QR kodunun yolu döndürülüyor.

