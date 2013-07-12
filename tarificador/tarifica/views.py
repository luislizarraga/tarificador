# Create your views here.


from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from tarifica.forms import AddProviderInfo


def setupUno(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AddProviderInfo(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            monthly_cost = form.cleaned_data['monthly_cost']
            period_end = form.cleaned_data['period_end']
            payment_type = form.cleaned_data['payment_type']
            channels = form.cleaned_data['channels']
            p = Provider(name, monthly_cost, payment_type, channels)
            p.save()
            return HttpResponseRedirect('tarifica/thanks') # Redirect after POST
    else:
        form = AddProviderInfo() # An unbound form

    return render(request, 'tarifica/contact.html', {
        'form': form,
    })



def thanks(request):
    return HttpResponse("jaja")