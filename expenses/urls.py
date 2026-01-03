from django.urls import path
from . import views

urlpatterns = [
    # Category
    path("create_category/", views.create_category, name="create_category"),
    path("category_list/", views.category_list, name="category_list"),
    path("category_detail/<int:id>/", views.category_detail, name="category_detail"),
    path("update_category/<int:id>/", views.update_category, name="update_category"),
    path("delete_category/<int:id>/", views.delete_category, name="delete_category"),
    # Expense
    path("create_expense/", views.create_expense, name="create_expense"),
    path("", views.expense_list, name="expense_list"),
    path("expense_detail/<int:id>/", views.expense_detail, name="expense_detail"),
    path("update_expense/<int:id>/", views.update_expense, name="update_expense"),
    path("delete_expense/<int:id>/", views.delete_expense, name="delete_expense"),
]
