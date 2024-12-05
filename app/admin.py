from django.contrib import admin
from .models import (
    SSHActivity, SSHCruise, SSHInvoice, SSHPackages, SSHPassenger,
    SSHPayment, SSHPort, SSHRestaurant, SSHSides, SSHStateroom, SSHTrip, SSHTripPort, SSHEntertainmentActivity
)

admin.site.register(SSHActivity)
admin.site.register(SSHCruise)
admin.site.register(SSHInvoice)
# admin.site.register(SSHPackageInfo)
admin.site.register(SSHPackages)
admin.site.register(SSHPassenger)
admin.site.register(SSHPayment)
admin.site.register(SSHPort)
admin.site.register(SSHRestaurant)
admin.site.register(SSHSides)
admin.site.register(SSHStateroom)
admin.site.register(SSHTrip)
admin.site.register(SSHTripPort)
admin.site.register(SSHEntertainmentActivity)

