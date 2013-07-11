# Create your views here.


from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from tarifica.forms import AddProviderInfo

def setupUno(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AddProviderInfo(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            lala = form.cleaned_data['name']
            # ...
            return HttpResponseRedirect('tarifica/thanks', name) # Redirect after POST
    else:
        form = AddProviderInfo() # An unbound form

    return render(request, 'tarifica/contact.html', {
        'form': form,
    })



def thanks(request):
    return HttpResponse("gracias!")