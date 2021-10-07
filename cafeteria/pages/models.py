
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pages (models.Model):
    title = models.CharField(verbose_name= "Nombre", max_length=30)
    content = RichTextField(verbose_name="Contenido", null=True, blank=True)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ("title",)

    def __str__(self):
        return self.title
