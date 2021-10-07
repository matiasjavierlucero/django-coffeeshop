from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Categoria", null=False, blank=False)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']

    def __str__(self):
        return self.name


class Post (models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo", null=False, blank=False)
    content = models.TextField(blank=False, verbose_name="Contenido", null=False)
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor",on_delete=models.CASCADE) #USER
    categories = models.ManyToManyField(Category, verbose_name="Categoria", related_name= "get_posts")  #ES EL NOMBRE PARA HACE LA BUSQUEDA INVERSA EN JINJA,
                                                                                                        #POR EJEMPLO {% for post in category.get_posts.all %}
                                                                                                        #REEMPLAZA A category.post_set.all
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created']