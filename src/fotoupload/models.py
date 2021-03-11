import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


class Foto(models.Model):
    item = models.ImageField(upload_to='images/')
    info = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.item = self.compressFoto(self.item)
        super(Foto, self).save(*args, **kwargs)

    def compressFoto(self, item):
        imageTemproary = Image.open(item)
        outputIoStream = BytesIO()
        imageTemproary.save(outputIoStream , format='JPEG', quality=50)
        outputIoStream.seek(0)
        item = InMemoryUploadedFile(
            outputIoStream, 
            'ImageField', 
            "%s.jpg" % item.name.split('.')[0], 
            'image/jpeg', 
            sys.getsizeof(outputIoStream), 
            None
        )
        return item
