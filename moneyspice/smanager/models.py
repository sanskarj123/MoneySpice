from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

CATEGORY_CHOICES = (
    ("FD", "Food"),
    ("SH", "Shopping"),
    ("TR", "Transport"),
    ("FU", "Fuel"),
    ("EN", "Entertainment"),
    ("HL", "Health"),
    ("BL", "Bills"),
    ("OT", "Others"),
)

MODE_CHOICES = (
    ("ON", "Online"),
    ("OF", "Offline")
)

class Expense(models.Model):
    """
    """
    exp_date = models.DateTimeField(verbose_name="Expense Date")
    category = models.CharField(
            _("Expense Category"),
            max_length = 20,
            choices = CATEGORY_CHOICES,
            default = 'OT')
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
            default = 'OF'
    )
    
    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
