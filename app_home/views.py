from django.shortcuts import render, redirect
from django.contrib import messages # For displaying messages to the user
import requests  # For sending Telegram messages
from django.core.mail import send_mail # For sending emails
from django.conf import settings
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

            # Send email notification to the site admin
            try:
                send_mail(
                    'New Contact Form Submission',
                    f'You have received a new message from your website contact form:\n\n'
                    f'Name: {contact_submission.name}\n'
                    f'Contact: {contact_submission.contact}\n'
                    f'Message: {contact_submission.message}',
                    settings.DEFAULT_FROM_EMAIL,  # Use the email defined in settings
                    [settings.CONTACT_EMAIL_RECIPIENT],  # Send to configured recipient
                    fail_silently=False,
                )
            except Exception as e:
                # If email sending fails, log the error but don't break the form submission
                print(f"Error sending email: {e}")
                # Still show success message as the submission was saved to database

            # Send Telegram notification to the group
            try:
                telegram_bot_token = settings.BOT_TOKEN
                telegram_chat_id = settings.CHAT_ID
                if telegram_bot_token and telegram_chat_id:
                    telegram_message = f'Новое сообщение с сайта:\n\nИмя: {contact_submission.name}\nКонтакт: {contact_submission.contact}\nСообщение: {contact_submission.message}'
                    telegram_url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
                    telegram_payload = {
                        'chat_id': telegram_chat_id,
                        'text': telegram_message,
                        'parse_mode': 'HTML'
                    }
                    response = requests.post(telegram_url, data=telegram_payload)
                    if response.status_code != 200:
                        print(f"Error sending Telegram message: {response.status_code} - {response.text}")
            except Exception as e:
                return redirect("home")
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
