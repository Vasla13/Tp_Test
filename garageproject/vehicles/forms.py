from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'purchase_date', 'number_of_seats', 'description', 'length', 'has_air_conditioning']
        labels = {
            'brand': 'Marque',
            'purchase_date': "Date d'achat",
            'number_of_seats': 'Nombre de places',
            'description': 'Description',
            'length': 'Longueur du véhicule',
            'has_air_conditioning': 'Climatisation',
        }
