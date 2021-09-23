from django.contrib import admin
from .models import phoneNumbers,Outbox, Inbox, DeliveryReport

admin.site.register(phoneNumbers)
admin.site.register(Outbox)
admin.site.register(Inbox)
admin.site.register(DeliveryReport)