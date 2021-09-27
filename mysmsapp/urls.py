from django.urls import path
from . import views
app_name = "mysmsapp"

urlpatterns = [

    path('sendsms/', views.send_me_sms, name="sendSms"),

]