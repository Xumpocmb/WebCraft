from django.shortcuts import render, redirect
from django.contrib import messages # For displaying messages to the user
from django.core.mail import send_mail # For sending emails
from .models import Service, Price
from .forms import ContactForm # Import the ContactForm

# Create your views here.

def home(request):
    services = Service.objects.all()
    prices = Price.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_submission = form.save()
            
            # Send email notification
            send_mail(
                'New Contact Form Submission',
                f'Name: {contact_submission.name}\nContact: {contact_submission.contact}\nMessage: {contact_submission.message}',
                'webmaster@localhost', # Replace with your sender email
                ['your_email@example.com'], # Replace with recipient email(s)
                fail_silently=False,
            )
            
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('home') # Redirect to the home page (or a success page)
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ContactForm() # An unbound form for GET request

    context = {
        'services': services,
        'prices': prices,
        'form': form, # Pass the form to the context
    }
    return render(request, 'index.html', context)
