from django.db import models

class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ])

    class Meta:
        managed = False
        db_table = 'ssh_passenger'


class Stateroom(models.Model):
    stateroom_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30)
    size = models.IntegerField()

    class Meta:
        db_table = 'ssh_stateroom'

    def __str__(self):
        return self.type  # Display stateroom type in dropdowns


class Side(models.Model):
    side_id = models.AutoField(primary_key=True)
    side_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'ssh_sides'

    def __str__(self):
        return self.side_name  # Display side name in dropdowns


class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'ssh_packages'

    def __str__(self):
        return self.package_name  # Display package name in dropdowns



class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    room_cost = models.DecimalField(max_digits=10, decimal_places=2)
    package_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ssh_invoice'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ssh_payment'


# from django.db import models

# class Port(models.Model):
#     port_id = models.SmallIntegerField(primary_key=True, help_text="Unique identifier for each port")
#     name = models.CharField(max_length=30, help_text="Name of the port")
#     state = models.CharField(max_length=30, help_text="State where the port is located")
#     country = models.CharField(max_length=30, help_text="Country where the port is located")
#     street_address = models.CharField(max_length=30, help_text="Street address of the port")
#     zip_code = models.CharField(max_length=6, help_text="ZIP or postal code of the port location")
#     nearest_airport_name = models.CharField(max_length=30, help_text="Nearest airport to the port")
#     number_of_parking_spots = models.SmallIntegerField(help_text="Number of parking spots available at the port")

#     class Meta:
#         db_table = "ssh_port"  # Map this model to the existing MySQL table
#         managed = False  # Prevent Django from creating, altering, or deleting this table
#         verbose_name = "Port"
#         verbose_name_plural = "Ports"

#     def __str__(self):
#         return self.name

# # Create booking system to book a trip. I want add-passenger pages. where in passenger inetrs info required in the db except the passengerid as its auto generated if the passenger is already there in the db update or not update acc and if not there insert it. Ask for preferences for each passenger like staerooms dropdown, sides, packages(can select multiple). Make this for multiple passenger. Get all this data so that I can add in the respective tables. Give me code for django.