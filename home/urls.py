from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='index'),
    path('hakkimizda/',views.hakkimizda, name='hakkkimizda'),
    path('referanslar/',views.referanslar, name='referanslar'),
    path('iletisim/',views.iletisim, name='iletisim'),

]