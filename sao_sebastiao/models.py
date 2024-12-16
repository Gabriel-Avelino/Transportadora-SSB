from django.db import models
from django.contrib.auth.models import User
from django.db import models
import uuid 
from unicodedata import normalize

# Create your models here.
def uploadFotoImovel(instance, filename):
    return 'imoveis/{}-{}'.format(str(uuid.uuid4()), filename)

class Tipo_doc (models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Tipos docs"

class Documento (models.Model):
    name_doc = models.CharField(max_length=255)
    tipo = models.ForeignKey(Tipo_doc, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents')

    def __str__(self):
        return self.name_doc
    
    def save(self, *args, **kwargs):
        self.file.name = normalize('NFKD', self.file.name).encode('ascii', 'ignore').decode('ascii')
        existing_doc = Documento.objects.filter(name_doc=self.name_doc, tipo=self.tipo).first()
        
        if existing_doc:
            existing_doc.file.delete(save=False)  # Delete the old file from disk
            existing_doc.file = self.file  # Update the file with the new one
            existing_doc.tipo = self.tipo  # Update tipo if necessary
            super(Documento, existing_doc).save(*args, **kwargs)  # Save the existing document
        else:
            super(Documento, self).save(*args, **kwargs)