from django.shortcuts import render, redirect
from .models import Transaction


def finance_home(request):
    transactions = Transaction.objects.all()

    total_income = sum(
        t.amount for t in transactions if t.transaction_type == 'Income'
    )

    total_expense = sum(
        t.amount for t in transactions if t.transaction_type == 'Expense'
    )

    balance = total_income - total_expense

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }

    return render(request, 'finances/index.html', context)


def add_transaction(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        transaction_type = request.POST.get('transaction_type')
        description = request.POST.get('description')

        Transaction.objects.create(
            title=title,
            amount=amount,
            transaction_type=transaction_type,
            description=description
        )

        return redirect('finance_home')

    return render(request, 'finances/add_transaction.html')
