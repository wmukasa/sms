import requests
from django.db import models
from django.conf import settings
import africastalking
class phoneNumbers(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.name
        
class Outbox(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    statusCode = models.IntegerField()
    phone = models.CharField(max_length=15)
    text = models.CharField(max_length=255)
    messageId = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date',)
        verbose_name = ("Outbox")
        verbose_name_plural = ("Outbox")

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.messageId, self.status, self.text[:10])  # noqa: E501

    @staticmethod
    def send(phone_number, message):
        username = "wmukasa"   
        api_key = "db6816cf46dde48c18b17055b769e8f75e253ba08cc5db8e93e0a8923300fc09"      
        africastalking.initialize(username, api_key)
        sms = africastalking.SMS
        my_phones =[]
        phone_set = phoneNumbers.objects.exclude(phone='').values_list('phone')
        for contact in phone_set:
            my_phones.append(contact[0])
        phone_number=my_phones
        response = sms.send(message,phone_number)
        # url = settings.AT_ENDPOINT_URL
        # headers = {'ApiKey': settings.AT_API_KEY,
        #            'Content-Type': 'application/x-www-form-urlencoded',
        #            'Accept': 'application/json'}
        # body = {'username': settings.AT_USER_NAME,
                
        #         'message': message,
        #         'to': phone_number}
        # response = requests.post(url=url, headers=headers, data=body)

        # data = response.json().get('SMSMessageData').get('Recipients')[0]
        # print(data)
    
        # Outbox_object = Outbox(status=data['status'],
        #                        statusCode=data['statusCode'],
        #                        phone=data['number'],
        #                        text=message,
        #                        messageId=data['messageId'])
        # Outbox_object.save()
        for recipient in response['SMSMessageData']['Recipients']:
            #number = recipient['number']
            status = recipient['status']
            statusCode = recipient['statusCode']
            phone = recipient['number']
            text = message
            messageId = recipient['messageId']
            Outbox.objects.create(status=status,statusCode=statusCode,
                                    phone=phone,text=text,messageId=messageId)      

class Inbox(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    text = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    to = models.IntegerField()
    linkId = models.CharField(max_length=100)

    class Meta:
        ordering = ('-date',)
        verbose_name = ("Inbox")
        verbose_name_plural = ("Inbox")

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.linkId, self.phone, self.text[:10])  # noqa: E501


class DeliveryReport(models.Model):
    identifier = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    phoneNumber = models.CharField(max_length=15)
    retryCount = models.IntegerField()
    status = models.CharField(max_length=10, blank=True, null=True)
    networkCode = models.IntegerField()

    class Meta:
        ordering = ('-date',)
        verbose_name = ("Delivery Report")
        verbose_name_plural = ("Delivery Reports")

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.identifier, self.phoneNumber, self.status)  # noqa: E501

