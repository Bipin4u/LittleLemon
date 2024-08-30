# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.core.mail import send_mail
from django.conf import settings



def menu(request):
    menu_data = Menu.objects.all()
    menu_data = {"menu" : menu_data}
    return render(request , 'menu.html' , menu_data)

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def book(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form':form}
#     return render(request, 'book.html', context)

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # Email content
            subject = 'Booking Confirmation'
            plain_message = (
                f'Thank you {booking.first_name} {booking.last_name} for your booking! '
                f'We have received your request with the following comment: "{booking.comment}". '
                f'We will process it shortly.'
            )
            html_message = (
                f'<p>Thank you {booking.first_name} {booking.last_name} for your booking!</p>'
                f'<p>We have received your request with the following comment:</p>'
                f'<blockquote>{booking.comment}</blockquote>'
                f'<p>We will process it shortly.</p>'
            )
            recipient_email = booking.email
            sender_email = settings.DEFAULT_FROM_EMAIL

            send_mail(
                subject,
                plain_message,  # For email clients that do not support HTML
                sender_email,
                [recipient_email],
                fail_silently=False,
                html_message=html_message  # For email clients that support HTML
            )

    context = {'form': form}
    return render(request, 'book.html', context)

def menu_item(request , pk ):
    if(pk):
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = []
    context = {'menu_item': menu_item}
    return render(request, 'menu_item.html', context)