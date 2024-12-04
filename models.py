# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SshCruise(models.Model):
    ssh_trip_trip = models.OneToOneField('SshTrip', models.DO_NOTHING, primary_key=True, db_comment='Unique identifier for each trip')  # The composite primary key (ssh_trip_trip_id, ssh_passenger_passenger_id, group_id) found, that is not supported. The first column is selected.
    ssh_passenger_passenger = models.ForeignKey('SshPassenger', models.DO_NOTHING, db_comment='Unique identifier for each passenger')
    group_id = models.CharField(max_length=5, db_comment='Identifier for the passenger group on the cruise')
    ssh_stateroom_stateroom = models.ForeignKey('SshStateroom', models.DO_NOTHING, db_comment='Stateroom assigned to the passenger')
    ssh_sides_side = models.ForeignKey('SshSides', models.DO_NOTHING, db_comment='Side of the ship assigned for the passenger')
    ssh_restaurant_restaurant = models.ForeignKey('SshRestaurant', models.DO_NOTHING, db_comment='Restaurant assigned to the passenger')
    ssh_invoice_invoice = models.OneToOneField('SshInvoice', models.DO_NOTHING, db_comment='Invoice associated with the trip')
    ssh_ent_act_ent = models.ForeignKey('SshEntAct', models.DO_NOTHING, db_comment='Entertainment activity assigned')
    ssh_ent_act_floor_number = models.ForeignKey('SshEntAct', models.DO_NOTHING, db_column='ssh_ent_act_floor_number', to_field='floor_number', related_name='sshcruise_ssh_ent_act_floor_number_set', db_comment='Floor number where entertainment activity takes place')

    class Meta:
        managed = False
        db_table = 'ssh_cruise'
        unique_together = (('ssh_trip_trip', 'ssh_passenger_passenger', 'group_id'),)


class SshEntAct(models.Model):
    ent_id = models.IntegerField(primary_key=True, db_comment='Unique identifier for each entertainment activity')  # The composite primary key (ent_id, floor_number) found, that is not supported. The first column is selected.
    floor_number = models.IntegerField(db_comment='Floor number for the entertainment activity')
    type = models.CharField(max_length=30, db_comment='Type of entertainment activity (e.g., Theater, Casino)')

    class Meta:
        managed = False
        db_table = 'ssh_ent_act'
        unique_together = (('ent_id', 'floor_number'),)


class SshInvoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True, db_comment='Unique identifier for each invoice')
    date = models.DateField(db_column='Date', db_comment='Date the invoice was issued')  # Field name made lowercase.
    due_date = models.DateField(db_comment='Due date for the invoice payment')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, db_comment='Total amount charged on the invoice')
    payment_method = models.CharField(max_length=30, blank=True, null=True, db_comment='Payment method for the invoice (e.g., Credit Card, Cash)')
    room_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment='Cost of the room assigned for the trip')
    package_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment='Cost of the package chosen by the passenger')

    class Meta:
        managed = False
        db_table = 'ssh_invoice'


class SshPackageInfo(models.Model):
    package = models.OneToOneField('SshPackages', models.DO_NOTHING, primary_key=True, db_comment='Unique identifier for each package')  # The composite primary key (package_id, trip_id, passenger_id, group_id) found, that is not supported. The first column is selected.
    trip = models.ForeignKey(SshCruise, models.DO_NOTHING, db_comment='Identifier for the trip associated with the package')
    passenger = models.ForeignKey(SshCruise, models.DO_NOTHING, to_field='ssh_passenger_passenger_id', related_name='sshpackageinfo_passenger_set', db_comment='Identifier for the passenger associated with the package')
    group = models.ForeignKey(SshCruise, models.DO_NOTHING, to_field='group_id', related_name='sshpackageinfo_group_set', db_comment='Identifier for the group associated with the package')

    class Meta:
        managed = False
        db_table = 'ssh_package_info'
        unique_together = (('package', 'trip', 'passenger', 'group'),)


class SshPackages(models.Model):
    package_id = models.IntegerField(primary_key=True, db_comment='Unique identifier for each package')
    package_name = models.CharField(max_length=30, db_comment='Name of the package (e.g., Luxury Package)')
    cost = models.DecimalField(max_digits=3, decimal_places=0, db_comment='Cost of the package')

    class Meta:
        managed = False
        db_table = 'ssh_packages'


class SshPassenger(models.Model):
    passenger_id = models.CharField(primary_key=True, max_length=5, db_comment='Unique identifier for each passenger')
    date_of_birth = models.DateField(db_comment='Passenger’s date of birth')
    first_name = models.CharField(max_length=30, db_comment='Passenger’s first name')
    last_name = models.CharField(max_length=30, db_comment='Passenger’s last name')
    street_address = models.CharField(max_length=30, db_comment='Street address of the passenger')
    city = models.CharField(max_length=30, db_comment='City of the passenger')
    state = models.CharField(max_length=30, db_comment='State of residence for the passenger')
    country = models.CharField(max_length=30, db_comment='Country of residence for the passenger')
    zip_code = models.CharField(max_length=6, db_comment='ZIP or postal code of the passenger')
    phone_number = models.CharField(max_length=15, db_comment='Passenger’s contact phone number')
    blood_group = models.CharField(max_length=5, db_comment='Passenger’s blood group')

    class Meta:
        managed = False
        db_table = 'ssh_passenger'


class SshPayment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=5, db_comment='Unique identifier for each payment')
    payment_date = models.DateField(db_comment='Date when the payment was made')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, db_comment='Amount paid by the passenger')
    payment_method = models.CharField(max_length=30, db_comment='Payment method used for the transaction')
    ssh_invoice_invoice = models.ForeignKey(SshInvoice, models.DO_NOTHING, db_comment='Invoice identifier associated with this payment')

    class Meta:
        managed = False
        db_table = 'ssh_payment'


class SshPort(models.Model):
    port_id = models.IntegerField(primary_key=True, db_comment='Unique identifier for each port')
    name = models.CharField(max_length=30, db_comment='Name of the port')
    state = models.CharField(max_length=30, db_comment='State where the port is located')
    country = models.CharField(max_length=30, db_comment='Country where the port is located')
    street_address = models.CharField(max_length=30, db_comment='Street address of the port')
    zip_code = models.CharField(max_length=6, db_comment='ZIP code for the port location')
    nearest_airport_name = models.CharField(max_length=50, db_comment='Nearest airport to the port')
    number_of_parking_spots = models.SmallIntegerField(db_comment='Number of parking spots available at the port')

    class Meta:
        managed = False
        db_table = 'ssh_port'


class SshRestaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True, db_comment='Unique identifier for each restaurant on the cruise')
    name = models.CharField(max_length=30, db_comment='Name of the restaurant')
    type = models.CharField(max_length=30, db_comment='Type of restaurant (e.g., Buffet, Fine Dining)')
    opening_hours = models.TimeField(db_comment='Opening time of the restaurant')
    closing_hours = models.TimeField(db_comment='Closing time of the restaurant')
    floor = models.IntegerField(db_comment='Floor where the restaurant is located')

    class Meta:
        managed = False
        db_table = 'ssh_restaurant'


class SshSides(models.Model):
    side_id = models.IntegerField(primary_key=True, db_comment='Unique identifier for each side of the ship')
    side_name = models.CharField(max_length=30, db_comment='Name of the side (e.g., Left, Right)')
    description = models.CharField(max_length=20, db_comment='Description of the view or location for this side')

    class Meta:
        managed = False
        db_table = 'ssh_sides'


class SshStateroom(models.Model):
    stateroom_id = models.IntegerField(primary_key=True, db_comment='Unique identifier for each stateroom on the ship')
    type = models.CharField(max_length=30, db_comment='Type of stateroom (e.g., Suite, Deluxe)')
    size = models.SmallIntegerField(db_column='Size', db_comment='Size of the stateroom in square feet')  # Field name made lowercase.
    number_of_bed = models.IntegerField(db_comment='Number of beds in the stateroom')
    number_of_bathrooms = models.DecimalField(max_digits=2, decimal_places=1, db_comment='Number of bathrooms in the stateroom')
    balcony = models.IntegerField(db_comment='Indicates if the stateroom has a balcony (1 = Yes, 0 = No)')

    class Meta:
        managed = False
        db_table = 'ssh_stateroom'


class SshTrip(models.Model):
    trip_id = models.CharField(primary_key=True, max_length=5, db_comment='Unique identifier for each cruise trip')
    total_nights = models.SmallIntegerField(db_comment='Total number of nights for the trip')
    start_port = models.CharField(max_length=30, db_comment='Name of the port where the trip begins')
    end_port = models.CharField(max_length=30, db_comment='Name of the port where the trip ends')
    port_stops = models.IntegerField(db_comment='Number of port stops included in the trip')

    class Meta:
        managed = False
        db_table = 'ssh_trip'


class SshTripPort(models.Model):
    start_time = models.DateField(db_comment='Date and time when the ship arrives at this port')
    end_time = models.DateField(db_comment='Date and time when the ship departs from this port')
    port = models.ForeignKey(SshPort, models.DO_NOTHING, db_comment='Unique identifier for the port where the stop occurs')
    trip = models.OneToOneField(SshTrip, models.DO_NOTHING, primary_key=True, db_comment='Unique identifier for the trip associated with the port stop')  # The composite primary key (trip_id, port_id) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'ssh_trip_port'
        unique_together = (('trip', 'port'),)
