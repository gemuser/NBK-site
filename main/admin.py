
from django.contrib import admin
from .models import Notification, GalleryImage, Department

admin.site.register(Notification)
from .models import Message
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'uploaded_on']



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    
from django.contrib import admin

admin.site.site_header = "NBK polytechnical institute"
admin.site.site_title = "College Admin Portal"
admin.site.index_title = "Welcome to the Admin Dashboard"


