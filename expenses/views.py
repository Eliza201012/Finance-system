from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from .forms import CategoryForm, ExpenseForm
from accounts.models import Profile

# CRUD (Category)
@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Категорія успішно створена!;)")
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "category/category_form.html", {"form" : form})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, "category/category_list.html", {"categories" : categories})

@login_required
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, "category/category_detail.html", {"category" : category})

@login_required
def update_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Категорія успішно оновлена!")
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "category/category_form.html", {"form" : form})

@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Категорія успішно видалена!")
        return redirect("category_list")
    return render(request, "category/category_confirm_delete.html", {"category" : category})


# CRUD (Expense)
@login_required
def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # Після валідації джанго кладе результат у словник form.cleaned_data
            amount = form.cleaned_data["amount"]
            profile = Profile.objects.get(user=request.user)

            if profile.balance < amount:
                messages.error(request, "Dude, you're broke")
            else:
                # Щоб користувач зміг щось додати або змінити перед збереженням
                expense = form.save(commit=False)
                # Ця витрата належить поточному залогіненому користувачу
                expense.user = request.user

                profile.balance -= amount
                profile.save()

                expense.save()
                messages.success(request, "Витрата успішно створена!:)")
                return redirect("expense_list")
    else:
        form = ExpenseForm()
    return render(request, "expenses/expense_form.html", {"form" : form})

@login_required
def expense_list(request):
    # Фільтруємо і виводимо витрати поточного користувача
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "expenses/expense_list.html", {"expenses" : expenses})

@login_required
def expense_detail(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    return render(request, "expenses/expense_detail.html", {"expense" : expense})

@login_required
def update_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Витрата успішно оновлена!")
            return redirect("expense_list")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "expenses/expense_form.html", {"form" : form})

@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        # Повертаємо гроші
        profile.balance += expense.amount
        profile.save()

        expense.delete()

        messages.success(request, "Витрата успішно видалена, гроші повернені на баланс!")
        return redirect("expense_list")
    
    return render(request, "expenses/expense_confirm_delete.html", {"expense" : expense})