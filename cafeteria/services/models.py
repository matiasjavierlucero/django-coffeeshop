from django.db import models

# Create your models here.
class Service (models.Model):
    Title = models.CharField(max_length=200, verbose_name="Titulo", null=False, blank=False)
    Subtitle = models.CharField(max_length=200, verbose_name="Subtitulo", null=False, blank=False)
    Content = models.TextField(blank=False, verbose_name="Contenido", null=False)
    Image = models.ImageField(upload_to='services')
    Created = models.TimeField(auto_now_add=True)
    Updated = models.TimeField(auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-Created']