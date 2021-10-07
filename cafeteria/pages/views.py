from django.shortcuts import get_object_or_404, render
from .models import Pages
# Create your views here.


def page(request, page_id):
    pages = Pages.objects.all()
    return render(request, 'pages/sample.html', {'pages':pages})


