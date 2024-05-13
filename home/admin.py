from django.contrib import admin
from home.models import Setting, ContactFormMessage

# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'note', 'status']


admin.site.register(ContactFormMessage,ContactFormMessageAdmin)

admin.site.register(Setting,SettingAdmin)