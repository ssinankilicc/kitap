from django.shortcuts import render
from home.models import Setting, ContactFormMessage, ContactFormu
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request, 'referanslar.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)

        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız iletilmiştir. Teşekkürler.")
            return HttpResponseRedirect ('/iletisim')

    setting = Setting.objects.get()
    form = ContactFormu()
    context = {'setting':setting, 
               'form':form,
               }
    return render(request,'iletisim.html',context)