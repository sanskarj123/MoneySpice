from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    """Form class for Expense model
    
    Attributes:
        model: stores the name of model for the form
        fields: stores all the fields which will be shown to the user
        
    """
    class Meta:
        model = Expense
        fields = (
            'exp_date',
            'category',
            'description',
            'amount',
            'mode')
