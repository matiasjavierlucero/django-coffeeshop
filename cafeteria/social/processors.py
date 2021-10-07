from .models import Social

def ctx_dict(request):
    ctx = {}
    links = Social.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx