from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
# Create your views here.
days_description = {
    'monday': 'Monday is the first day of week',
    'tuesday': 'Tuesday is the second day of week',
    'wednesday': 'Wednesday is the third day of week',
    'thursday': 'Thrusday is the fourth day of week',
    'friday': 'Friday is the fifth day of week',
    'saturday': 'Saturday is the sixth day of week',
    'sunday': 'Sunday is the seventh day of week',
}


def index(request):
    return HttpResponse("you are on home page")

def int_day(request, int_day):
    days = list(days_description.keys())
    # validating day number 
    if int_day > len(days):
        return HttpResponseNotFound("Invalid Number")
    day = days[int_day - 1]
    redirect_path = reverse('day_by_number', args=[day])
    return HttpResponseRedirect(redirect_path)

def day_description(request, day):
    '''will return description of the entered day'''
    try:
        day_des = days_description[day]
        return HttpResponse(day_des)
    except:
        return HttpResponseNotFound("Invalid day")
