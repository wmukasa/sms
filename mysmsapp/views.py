from django.shortcuts import render
from django.http import HttpResponse
from .models import phoneNumbers,Sentsms
#from .helpers import SMS
import africastalking
def send_me_sms(request):
    #Initialize SDK
    username = "wmukasa"    # use 'wmukasa' for production in the real environment
    api_key = "db6816cf46dde48c18b17055b769e8f75e253ba08cc5db8e93e0a8923300fc09"      
    # use my  app API key for production in the real environment
    africastalking.initialize(username, api_key)
    #def home(request):
        #return HttpResponse('<h1>Hello WIlliam</h1>')
    # Initialize a service e.g. SMS
    sms = africastalking.SMS
    my_phones =[]
    phone_set = phoneNumbers.objects.exclude(phone='').values_list('phone')
    for contact in phone_set:
        my_phones.append(contact[0])
    print(my_phones)
    #sms.send("Hello Love, Sorry for continous Messages, am testing my application for sending sms to people", my_phones)
    #response = sms.send(*my_phones)
    response = sms.send("Hello Love, Sorry for continous Messages, am testing my application for sending sms to people", my_phones)
    print(response)
   
    # my_phones =[]
    # phone_set = phoneNumbers.objects.exclude(phone='').values_list('phone')
    # for contact in phone_set:
    #     my_phones.append(contact[0])
    # my_sms = SMS()
    # response = my_sms.send(*my_phones)
    # print(response)
    for recipient in response['SMSMessageData']['Recipients']:
        number = recipient['number']
        status = recipient['status']
        statusCode = recipient['statusCode']
        Sentsms.objects.create(number=number, status=status,statusCode=statusCode)
    
    print('Finished sending  messages')
    
    return HttpResponse('<h1>William  sending sms</h1>')


