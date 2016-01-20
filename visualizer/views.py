from django.shortcuts import render

from visualizer.models import (SSIAfr, SPI3Month)

def index(request):
    all_entries = SSIAfr.objects.order_by('date')
    ndvi_dates = [e.date for e in all_entries]
    SPI_entries = SPI3Month.objects.order_by('date')
    SPI_dates = [s.date for s in SPI_entries]
    return render(request, 'visualizer/index.html',
                  {'ndvi_dates': ndvi_dates, 'SPI_dates': SPI_dates})
