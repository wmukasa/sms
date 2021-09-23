from django.contrib import admin
from django.urls import path,include
from smsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('smsapp.urls')),
    path('',views.outbox,name='outbox'),
    path('smsapp/',include('smsapp.urls',namespace='smsapp')),
]




