from django import forms
from django.forms import formset_factory
from .models import Passenger, Stateroom, Side, Package

# Form for number of passengers
class NumPassengersForm(forms.Form):
    num_passengers = forms.IntegerField(
        min_value=1,
        label="Number of Passengers",
        widget=forms.NumberInput(attrs={'placeholder': 'Enter number of passengers'})
    )

# Form for individual passenger details
class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        exclude = ['passenger_id']

PassengerFormSet = formset_factory(PassengerForm, extra=0)  # Forms dynamically created

class PreferenceForm(forms.Form):
    # Fetch stateroom types dynamically
    stateroom = forms.ModelChoiceField(
        queryset=Stateroom.objects.all(),
        empty_label="Select Stateroom",
        to_field_name="type",
        label="Stateroom Type"
    )
    
    # Fetch side names dynamically
    side = forms.ModelChoiceField(
        queryset=Side.objects.all(),
        empty_label="Select Side",
        to_field_name="side_name",
        label="Side Name"
    )
    
    # Fetch package names dynamically
    packages = forms.ModelMultipleChoiceField(
        queryset=Package.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        to_field_name="package_name",
        label="Packages"
    )
# Form for payment
class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cash', 'Cash')],
        widget=forms.Select()
    )
