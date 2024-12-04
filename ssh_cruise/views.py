from django.shortcuts import render, redirect
from django.db import transaction
from django.utils.timezone import now, timedelta
from decimal import Decimal
from django.forms import formset_factory
from .models import Passenger, Stateroom, Side, Package, Invoice, Payment
from .forms import PassengerForm, PreferenceForm, PaymentForm, NumPassengersForm
import uuid
from django.db import connection


def calculate_cost(stateroom, packages):
    room_cost = stateroom.size * 2  # Example calculation
    package_cost = sum(package.cost for package in packages)
    total_cost = room_cost + package_cost
    return room_cost, package_cost, total_cost


def create_invoice(stateroom, packages):
    room_cost, package_cost, total_cost = calculate_cost(stateroom, packages)
    due_date = now().date() + timedelta(days=7)
    invoice = Invoice.objects.create(
        due_date=due_date,
        total_amount=Decimal(total_cost),
        room_cost=Decimal(room_cost),
        package_cost=Decimal(package_cost)
    )
    return invoice


def num_passengers(request):
    """Step 1: Ask for the number of passengers."""
    if request.method == 'POST':
        form = NumPassengersForm(request.POST)
        if form.is_valid():
            num_passengers = form.cleaned_data['num_passengers']
            request.session['num_passengers'] = num_passengers  # Store the value in the session
            return redirect('add_passenger')
    else:
        form = NumPassengersForm()
    return render(request, 'num_passengers.html', {'form': form})


@transaction.atomic
def add_passenger(request):
    """Step 2: Add passenger details."""
    num_passengers = request.session.get('num_passengers', 1)
    PassengerFormSet = formset_factory(PassengerForm, extra=num_passengers)

    if request.method == 'POST':
        passenger_formset = PassengerFormSet(request.POST)
        preference_form = PreferenceForm(request.POST)
        if passenger_formset.is_valid() and preference_form.is_valid():
            preferences = preference_form.cleaned_data
            group_id = uuid.uuid4().hex[:8].upper()  # Unique group ID
            passenger_ids = []

            for passenger_form in passenger_formset:
                passenger_data = passenger_form.cleaned_data
                passenger, created = Passenger.objects.update_or_create(
                    first_name=passenger_data['first_name'],
                    last_name=passenger_data['last_name'],
                    date_of_birth=passenger_data['date_of_birth'],
                    defaults=passenger_data
                )
                passenger_ids.append(passenger.passenger_id)

            stateroom = preferences['stateroom']
            packages = preferences['packages']

            # Create an invoice
            invoice = create_invoice(stateroom, packages)

            # Insert into ssh_cruise
            for passenger_id in passenger_ids:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO ssh_cruise (ssh_trip_trip_id, ssh_passenger_passenger_id, group_id, ssh_stateroom_stateroom_id, ssh_sides_side_id)
                        VALUES (%s, %s, %s, %s, %s)
                    """, ['TRIP01', passenger_id, group_id, stateroom.id, preferences['side'].id])

            # Insert into ssh_package_info
            for package in packages:
                for passenger_id in passenger_ids:
                    with connection.cursor() as cursor:
                        cursor.execute("""
                            INSERT INTO ssh_package_info (package_id, trip_id, passenger_id, group_id)
                            VALUES (%s, %s, %s, %s)
                        """, [package.id, 'TRIP01', passenger_id, group_id])

            return redirect('invoice', invoice_id=invoice.invoice_id)
    else:
        passenger_formset = PassengerFormSet()
        preference_form = PreferenceForm()
    return render(request, 'add_passenger.html', {'passenger_formset': passenger_formset, 'preference_form': preference_form})


def invoice_view(request, invoice_id):
    invoice = Invoice.objects.get(invoice_id=invoice_id)
    return render(request, 'invoice.html', {'invoice': invoice})


def add_payment(request, invoice_id):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            invoice = Invoice.objects.get(invoice_id=invoice_id)
            Payment.objects.create(
                payment_amount=invoice.total_amount,
                payment_method=payment_method,
                invoice=invoice
            )
            return redirect('success')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})


def success(request):
    return render(request, 'success.html')
