from django.db import models
from .utils import create_qr_code_image
# Create your models here.
class QrCode(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    scan_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        super(QrCode, self).save(*args, **kwargs)  # Önce modelin normal save metodu çağırılıyor.
        redirect_url = self.url
        create_qr_code_image(redirect_url, self.id)
        
    def __str__(self):
        return self.name
