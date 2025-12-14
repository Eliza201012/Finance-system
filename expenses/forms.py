from django import forms
from .models import Category, Expense

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label="Назва категорії",
                           widget=forms.TextInput(attrs={
                               "class" : "form-control",
                               "placeholder" : "Наприклад: їжа"
                           }))
    icon = forms.CharField(label="Іконка",
                           widget=forms.TextInput(attrs={
                               "class" : "form-control",
                               "placeholder" : "fa-solid fa-utensils"
                           }))
    class Meta:
        model = Category
        fields = ("name", "icon")


class ExpenseForm(forms.ModelForm):
    name = forms.CharField(label="Назва витрати",
                           widget=forms.TextInput(attrs={
                               "class" : "form-control",
                               "placeholder" : "Наприклад: продукти"
                           }))
    amount = forms.DecimalField(label="Сума",
                                widget=forms.NumberInput(attrs={
                                    "class" : "form-control",
                                    "step" : "1",
                                    "placeholder" : "0.00"
                                }))
    category = forms.ModelChoiceField(label="Категорія",
                                      queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={
                                          "class" : "form-select"
                                      }))
    payment = forms.CharField(label="Спосіб оплати",
                              widget=forms.TextInput(attrs={
                                  "class" : "form-control",
                                  "placeholder" : "Готівка / Картка"
                              }))
    class Meta:
        model = Expense
        fields = ("name", "amount", "category", "payment")