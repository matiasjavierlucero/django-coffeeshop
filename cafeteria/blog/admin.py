from django.contrib import admin
from .models import Category,Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','author','published', 'post_categories',)
    ordering = ('author','title')
    search_fields = ('title','content','author__username',) # Si quiero buscar en un campo de la relacion, tengo que usar el lookup
    date_hierarchy = 'published'  #Nos permite navegar por las fechas en la parte superior
    list_filter = ('author__username','categories__name')

    #CREAR PROPIO CAMPO PARA MOSTRAR LAS CATEGORIAS EN LA LISTA
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"  #LO RENOMBRO

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)