from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse


from .models import (
    SSHActivity, SSHCruise, SSHInvoice, SSHPackages, SSHPassenger,
    SSHPayment, SSHPort, SSHRestaurant, SSHSides, SSHStateroom, SSHTrip, SSHTripPort, SSHEntertainmentActivity
)


def index(request):


    trips = SSHTrip.objects.all()
    staterooms = SSHStateroom.objects.all()
    packages = SSHPackages.objects.all()
    ent_acts = SSHEntertainmentActivity.objects.all()

    context = {
        'trips': trips,
        'staterooms': staterooms,
        'packages': packages,
        'ent_acts': ent_acts
    }

    return render(request, 'cruise/home.html', context)





def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:
        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))
    

    