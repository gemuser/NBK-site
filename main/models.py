
from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='notifications/', blank=True, null=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.caption or "Gallery Image"

class Department(models.Model):
    name = models.CharField(max_length=100, null=True)
    short_description = models.CharField(max_length=255,blank=True, null=True)  # if this already exists
    detailed_description = models.TextField(blank=True, null=True)  # <-- NEW FIELD

    def __str__(self):
        return self.name

from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name or 'Anonymous'} - {self.subject or 'No Subject'}"

