
from django.shortcuts import render, redirect
from .models import Notification, GalleryImage, Department
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    notifications = Notification.objects.order_by('-posted_on')[:5]
    return render(request, 'main/home.html', {'notifications': notifications})

def about(request):
    return render(request, 'main/about.html')

from .models import Department

def departments(request):
    departments = Department.objects.all()
    return render(request, 'main/departments.html', {'departments': departments})


def notifications(request):
    notifications = Notification.objects.order_by('-posted_on')
    return render(request, 'main/notifications.html', {'notifications': notifications})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'main/gallery.html', {'images': images})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f"Message from {name} ({email})",
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )
            return render(request, 'main/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Message

from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # or redirect to a thank you page
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin/')
        else:
            messages.error(request, 'Invalid credentials or not an admin user.')
    return render(request, 'main/admin_login.html')




