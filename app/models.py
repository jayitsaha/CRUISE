from django.db import models

class SSHActivity(models.Model):
    activity_id = models.CharField(max_length=5, primary_key=True)
    ent_id = models.ForeignKey('SSHEntertainmentActivity', on_delete=models.CASCADE)
    trip = models.ForeignKey('SSHTrip', on_delete=models.CASCADE)
    passenger = models.ForeignKey('SSHPassenger', on_delete=models.CASCADE)
    group_id = models.ForeignKey('SSHCruise', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ssh_activity'
        unique_together = ('trip', 'passenger', 'group_id')


class SSHCruise(models.Model):
    group_id = models.AutoField(max_length=5, primary_key=True)
    trip = models.ForeignKey('SSHTrip', on_delete=models.CASCADE)
    passenger = models.ManyToManyField('SSHPassenger', related_name='cruises')
    stateroom = models.ForeignKey('SSHStateroom', on_delete=models.CASCADE)
    side = models.ForeignKey('SSHSides', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('SSHRestaurant', on_delete=models.CASCADE)
    invoice = models.ForeignKey('SSHInvoice', on_delete=models.CASCADE)
    packages = models.ManyToManyField('SSHPackages', null=True, blank=True)
    class Meta:
        db_table = 'ssh_cruise'


class SSHEntertainmentActivity(models.Model):
    ent_id = models.PositiveIntegerField()
    floor_number = models.PositiveIntegerField()
    type = models.CharField(max_length=30)

    class Meta:
        db_table = 'ssh_ent_act'
        unique_together = ('ent_id', 'floor_number')


class SSHInvoice(models.Model):
    invoice_id = models.PositiveIntegerField(primary_key=True)
    date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30, null=True, blank=True)
    room_cost = models.PositiveIntegerField()
    package_cost = models.PositiveIntegerField()

    class Meta:
        db_table = 'ssh_invoice'


# class SSHPackageInfo(models.Model):
#     package_id = models.ForeignKey('SSHPackages', on_delete=models.CASCADE)
#     # trip = models.ForeignKey('SSHTrip', on_delete=models.CASCADE)
#     # passenger = models.ForeignKey('SSHPassenger', on_delete=models.CASCADE)
#     group_id = models.ForeignKey('SSHCruise', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'ssh_package_info'
#         unique_together = ('package_id', 'trip', 'passenger', 'group_id')


class SSHPackages(models.Model):
    package_id = models.PositiveIntegerField(primary_key=True)
    package_name = models.CharField(max_length=30)
    cost = models.PositiveIntegerField()

    class Meta:
        db_table = 'ssh_packages'


class SSHPassenger(models.Model):
    passenger_id = models.CharField(max_length=5, primary_key=True)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5)

    class Meta:
        db_table = 'ssh_passenger'


class SSHPayment(models.Model):
    payment_id = models.CharField(max_length=5, primary_key=True)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30)
    invoice = models.ForeignKey('SSHInvoice', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ssh_payment'


class SSHPort(models.Model):
    port_id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    nearest_airport_name = models.CharField(max_length=30)
    number_of_parking_spots = models.PositiveIntegerField()

    class Meta:
        db_table = 'ssh_port'


class SSHRestaurant(models.Model):
    restaurant_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    opening_hours = models.TimeField()
    closing_hours = models.TimeField()
    floor = models.PositiveIntegerField()

    class Meta:
        db_table = 'ssh_restaurant'


class SSHSides(models.Model):
    side_id = models.PositiveIntegerField(primary_key=True)
    side_name = models.CharField(max_length=30)
    description = models.CharField(max_length=20)

    class Meta:
        db_table = 'ssh_sides'


class SSHStateroom(models.Model):
    stateroom_id = models.CharField(max_length=2, primary_key=True)
    type = models.CharField(max_length=30)
    size = models.PositiveIntegerField()
    number_of_bed = models.PositiveIntegerField()
    number_of_bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    balcony = models.PositiveIntegerField()

    class Meta:
        db_table = 'ssh_stateroom'


class SSHTripStateroomSide(models.Model):
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    side = models.ForeignKey('SSHSides', on_delete=models.CASCADE)
    trip = models.ForeignKey('SSHTrip', on_delete=models.CASCADE)
    stateroom = models.ForeignKey('SSHStateroom', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ssh_tr_sr_s'
        unique_together = ('side', 'trip', 'stateroom')


class SSHTrip(models.Model):
    trip_id = models.CharField(max_length=5, primary_key=True)
    total_nights = models.PositiveIntegerField()
    start_port = models.CharField(max_length=30)
    end_port = models.CharField(max_length=30)
    port_stops = models.PositiveIntegerField()

    class Meta:
        db_table = 'ssh_trip'


class SSHTripPort(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    port = models.ForeignKey('SSHPort', on_delete=models.CASCADE)
    trip = models.ForeignKey('SSHTrip', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ssh_trip_port'
        unique_together = ('trip', 'port')