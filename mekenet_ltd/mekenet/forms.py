from django.forms import ModelForm

from .models import CustomerSaving


class CustomerSavingForm(ModelForm):
    """ Create a form for saving """
    class Meta:
        model = CustomerSaving
        #fields = ['id', 'name', 'compulsary', 'voluntary','vocher', 'total']
        fields = '__all__'