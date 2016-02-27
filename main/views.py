from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from models import FabricStockInfo, GarmentProduction, Garment

# Create your views here.

class FabricStockUpdateForm(forms.Form):
    garment = forms.ModelChoiceField(queryset= Garment.objects.order_by("description"))
    quantity = forms.IntegerField(min_value=1)

def fabric_stock_update(request):
    if request.method == 'POST':
        form = FabricStockUpdateForm(request.POST)
        if form.is_valid():
            
            #return the results on the screen
            pass
    else:
        form = FabricStockUpdateForm()
        
    fabric_stock_infos = FabricStockInfo.objects.all().order_by('fabric__name')
    return render(request, 'fabric_stock_update.html',
                  {
                      'form': form,
                      'fabric_stock_infos': fabric_stock_infos
                  })

