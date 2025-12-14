from django.db import models
from django_icon_picker.field import IconField

class Category(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100, unique=True)
    icon = IconField(verbose_name="Icon", max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    amount = models.DecimalField(verbose_name="Amount", max_digits=12, decimal_places=2, default=0.00)
    date_time = models.DateTimeField(verbose_name="Date and time", auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    payment = models.CharField(verbose_name="Payment", max_length=50)

    class Meta:
        ordering = ["-date_time"]
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __str__(self):
        return self.name