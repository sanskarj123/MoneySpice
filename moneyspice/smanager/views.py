from django.shortcuts import render, get_object_or_404

from .models import Expense
from .forms import ExpenseForm


# Create your views here.
def index(request):
    """
    """
    return render(request, 'index.html')

def get_expense(request):
    """
    """
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(
        request, 
        'show_expense.html', 
        context=context)
