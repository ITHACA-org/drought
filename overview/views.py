from django.shortcuts import render

from visualizer.models import SSIAfr

def update(request):
    latest = SSIAfr.objects.order_by('date').reverse()[0]
    latest_date = latest.date
    return render(request, 'overview/update.html', 
                  {'latest_date': latest_date}) 
