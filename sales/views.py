from django.shortcuts import render
from .models import Salesrecord
from django.http import JsonResponse
from django.utils.safestring import SafeString
# Create your views here.

def sales_info(request):
    salesinfo=Salesrecord.objects.all()
    col=[
        { "data": "region" },
        { "data": "country" },
        { "data": "item_type" },
        { "data": "sale_channel" },
        { "data": "order_id" },
        { "data": "units_sold" },
        { "data": "unit_price" },
        { "data": "unit_cost" },
        { "data": "total_revenue" },
        {"data": "total_cost"},
        {"data":"total_profit"}
    ]
    data=[sale.get_data() for sale in salesinfo]
    #Modificaion of session is done with modified class
    request.session['sales']="Sales Data"
    #response={'data':data}
    return render(request,'sales/salesinfo.html',{'sales':SafeString(data),'cols':SafeString(col)})

##Display using same datatable code

def display(request):
    data=[
        {
            "name":       "Tiger Nixon",
            "position":   "System Architect",
            "salary":     "$3,120",
            "start_date": "2011/04/25",
            "office":     "Edinburgh",
            "extn":       5421
        },
        {
            "name": "Garrett Winters",
            "position": "Director",
            "salary": "5300",
            "start_date": "2011/07/25",
            "office": "Edinburgh",
            "extn": "8422"
        },
    ]
    columns= [
        { "data": "name" },
        { "data": "position" },
        { "data": "office" },
        { "data": "extn" },
        { "data": "start_date" },
        { "data": "salary" }
    ]
    return render(request,'sales/new_records.html',{'data':SafeString(data),'cols':SafeString(columns)})

##Json Request 
def sales_json(request):
    salesinfo=Salesrecord.objects.all()
    data=[sale.get_data() for sale in salesinfo]
    response={'data':data}
    return JsonResponse(response)



    