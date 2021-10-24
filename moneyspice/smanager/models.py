from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

CATEGORY_CHOICES = (
    ("Food", "FOD"),
    ("Shopping", "SHP"),
    ("Transport", "TRT"),
    ("Fuel", "FUL"),
    ("Entertainment", "ENT"),
    ("Health", "HLT"),
    ("Bills", "BIL"),
    ("Others", "OTH"),
)

MODE_CHOICES = (
    ("Online", "ON"),
    ("Offline", "OFF")
)

class Expense(models.Model):
    """Expense model stores the expense
    
    Attributes:
        exp_date: Date of expense.
        category: Category fo the expense. Example: Food, Bills, etc.
        description: Description of one for the expense.
        amount: Amount of expense in rupees.
        mode: Payment mode of the expense. Example: Online, Offline.

    """
    exp_date = models.DateTimeField(verbose_name="Expense Date")
    category = models.CharField(
            _("Expense Category"),
            max_length = 20,
            choices = CATEGORY_CHOICES,
            default = 'OTH')
    description = models.CharField(
            _("Description"), 
            max_length = 20)
    amount = models.IntegerField(
            verbose_name="Expense Amount",
            )
    mode = models.CharField(
            _("Payment Mode"),
            max_length = 20,
            choices = MODE_CHOICES,
            default = 'OFF'
    )
    
    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
