from django.db import models

# Create your models here.
class Social (models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100,unique= True)
    name = models.CharField(verbose_name= "Nombre", max_length=30)
    url = models.URLField(verbose_name="Url", max_length=200, null=True, blank=True)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = "Red"
        verbose_name_plural = "Redes Sociales"
        ordering = ("name",)

    def __str__(self):
        return self.name
