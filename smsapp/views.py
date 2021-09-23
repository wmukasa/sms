import datetime

from django.http import HttpResponse
from django.utils.timezone import make_aware
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from .models import phoneNumbers,Outbox, Inbox, DeliveryReport
from .forms import CreateSms
#from .helpers import SMS

'''
import africastalking

def send_me_sms(request):
    # Initialize SDK
    username = "sandbox"    # use 'sandbox' for development in the test environment
    api_key = "1ee6d078109c880a4382fe6a40739a91cae59960e54eaef86e1c2861c4200f8f"      # use your sandbox app API key for development in the test environment
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
    sms.send("Gd afternoon, on Sunday we're having our meeting for the INTRODUCTION &WEDDING CEREMONIES OF MUKASA WILLY WAMALA.At Mengo time 2PM Dr.Tonny 070292051", my_phones)
    #my_sms = SMS()
    #response = my_sms.send(*my_phones)
    #print(response)
    
    for recipent in response['SMSMessageData']['Recipients']:
        number = recipient['number']
        status = recipient['status']
        statusCode = recipient['statusCode']
        Outbox.objects.create(number=number, status=status,statusCode=statusCode)
    
    print('Finished sending  messages')
    
    return HttpResponse('')
'''
def outbox(request):
    outbox = Outbox.objects.all()
    search_term = ''
    clicked = request.GET.get('clicked', 'outbox')
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        outbox = outbox.filter(text__icontains=search_term)
    paginator = Paginator(outbox, 5)
    page = request.GET.get('page')
    outbox = paginator.get_page(page)
    context = {'outbox': outbox, 'active': clicked, 'search_term': search_term}
    return render(request, "smsapp/outbox.html", context)


def create_sms(request):
    form = CreateSms()
    if request.method == "POST":
        form = CreateSms(request.POST)
        if form.is_valid():

            my_phones =[]
            phone_set = phoneNumbers.objects.exclude(phone='').values_list('phone')
            for contact in phone_set:
                my_phones.append(contact[0])
            print(my_phones) 
            phone_number = my_phones
            message = form.cleaned_data.get("message")
            #while len(my_phones): 

            for cont in my_phones:
                if (my_phones.index(cont)==0):
                    print(cont)
                    Outbox.send(cont,message)
                if (my_phones.index(cont)==1):
                    print(cont)
                    Outbox.send(cont,message)
                if (my_phones.index(cont)==2):
                    print(cont)
                    Outbox.send(cont,message)
            return redirect('outbox')

    return render(request, "smsapp/createsms.html", {"form": form})


@csrf_exempt
@require_POST
def incoming_message(request):
    """
    sample incoming message from phone through AfricasTalking API
    {  'from': ['+2547278153xx'],
     'linkId': ['28a92cdf-2d63-4ee3-93df-4233d3de0356'],
       'text': ['heey this is a message from a phone'],
         'id': ['b68d0989-d856-494f-92ee-7c439e96e1d9'],
       'date': ['2021-01-14 08:10:15'],
         'to': ['17163'] }
    """
    date = request.POST.get('date')
    text = request.POST.get('text')
    phoneNo = request.POST.get('from')
    to = request.POST.get('to')
    linkId = request.POST.get('linkId')
    date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    aware_datetime = make_aware(date)
    Inbox_object = Inbox(
                        date=aware_datetime,
                        text=text,
                        phone=phoneNo,
                        to=to,
                        linkId=linkId
                        )
    Inbox_object.save()
    return HttpResponse(status=200)


@csrf_exempt
@require_POST
def incoming_delivery_reports(request):
    """
    sample delivery report from Africas Talking API
    {'phoneNumber': ['+254727815xx'],
      'retryCount': ['0'],
          'status': ['Success'],
     'networkCode': ['63902'],
              'id': ['ATXid_29bc0ee2e3566472cd947d2f2918ab2f']}>
    """
    phoneNumber = request.POST.get('phoneNumber')
    retryCount = request.POST.get('retryCount')
    status = request.POST.get('status')
    networkCode = request.POST.get('networkCode')
    identifier = request.POST.get('id')
    DeliveryReport_object = DeliveryReport(identifier=identifier,
                                           phoneNumber=phoneNumber,
                                           retryCount=retryCount,
                                           status=status,
                                           networkCode=networkCode)
    DeliveryReport_object.save()
    return HttpResponse(status=200)


def delivery_reports(request):
    clicked = request.GET.get('clicked')
    all_delivery_reports = DeliveryReport.objects.all()
    paginator = Paginator(all_delivery_reports, 5)
    page = request.GET.get('page')
    all_delivery_reports = paginator.get_page(page)
    context = {'all_delivery_reports': all_delivery_reports, 'active': clicked}
    return render(request, "smsapp/deliveryreports.html", context)


def inbox(request):
    clicked = request.GET.get('clicked')
    all_inbox_items = Inbox.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET.get('search')
        all_inbox_items = all_inbox_items.filter(text__icontains=search_term)
    paginator = Paginator(all_inbox_items, 5)
    page = request.GET.get('page')
    all_inbox_items = paginator.get_page(page)
    context = {
      "all_inbox_items": all_inbox_items, 'active': clicked, 'search_term': search_term  # noqa: E501
    }
    return render(request, "smsapp/inbox.html", context)
