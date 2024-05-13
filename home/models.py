from django.db import models
from django.forms import ModelForm, Textarea, TextInput


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=120)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=10)
    fax = models.CharField(blank=True, max_length=10)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=40)
    smtpemail = models.CharField(blank=True, max_length=40)
    smtppassword = models.CharField(blank=True, max_length=40)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField()
    contact = models.TextField()
    references = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
    )
    name = models.CharField(max_length=30)
    email = models.CharField(blank=True,max_length=50)
    phone = models.CharField(blank=True,max_length=10)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    note = models.CharField(blank=True,max_length=130)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name'     : TextInput(attrs={'size': '30','class': 'input', 'placeholder': 'Adınız Soyadınız'}),
            'email'     : TextInput(attrs={'size': '30','class': 'input', 'placeholder': 'Email Adresiniz'}),
            'phone'     : TextInput(attrs={'size': '29','class': 'input', 'placeholder': 'Telefon Numaranız'}),
            'subject'   : TextInput(attrs={'size': '28','class': 'input', 'placeholder': 'Konu'}),
            'message'   : Textarea(attrs={'class': 'input', 'placeholder': 'Mesajınız', 'rows': '5'}),
        }
