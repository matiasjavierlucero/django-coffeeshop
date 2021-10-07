from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            #Enviamos email, redireccionamos
            email = EmailMessage(
                "Consulta la Caffetiera",
                f"""De <h1>{name}</h1>, <{email}> \n {content}""",
                "no-contestar@inbox.mailtrap.io",
                ["matias.lucero@comprandoengrupo.net"],
                reply_to=[email]
            )
            try:
                email.send()
            except Exception as error:
                return redirect(reverse('contact')+f"?{error}")
            return redirect(reverse('contact')+"?ok")

    return render(request, "contact/contact.html", {'form':contact_form} )