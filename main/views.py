from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from models import FabricStockInfo, GarmentProduction, Garment, Fabric,FabricBolt


#select a garment#
#input quantity made#
#select bolt(s) used#
#compute number of yards used (instances?)#
# display number of yards used on the screen#
#submit to remove yards used quantity from the data base#

class FabricStockUpdateForm(forms.Form):
    garment = forms.ModelChoiceField(queryset= Garment.objects.order_by("description"))
    quantity = forms.IntegerField(min_value=1)
    bolts = forms.ModelMultipleChoiceField(queryset=FabricBolt.objects.all(), widget=forms.CheckboxSelectMultiple(), required=True)
    yards_used = forms.IntegerField()
    
def fabric_stock_update(request):
    if request.method == 'POST':
        form = FabricStockUpdateForm(request.POST)
        if form.is_valid():
            
            #return the results on the screen
            pass
    else:
        form = FabricStockUpdateForm()
        
    fabrics = Fabric.objects.all().order_by('name')
    garments = Garment.objects.all().order_by('description')
    
    return render(request, 'fabric_stock_update.html',
                  {
                      'form': form,
                      'fabrics': fabrics,
                      'garments': garments,
                      
                  })

