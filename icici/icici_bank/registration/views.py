from django.shortcuts import render, redirect
from .forms import CustomerForm, SavingsAccountForm
from .models import Customer

def generate_customer_id():
    last_customer = Customer.objects.all().order_by('id').last()
    if not last_customer:
        return 'CID_5001'
    last_id = int(last_customer.customer_id.split('_')[1])
    new_id = last_id + 1
    return f'CID_{new_id}'

def register_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.customer_id = generate_customer_id()
            customer.save()
            return redirect('products', customer_id=customer.customer_id)
    else:
        form = CustomerForm()
    return render(request, 'registration/register.html', {'form': form})

def products(request, customer_id):
    return render(request, 'registration/products.html', {'customer_id': customer_id})

def open_savings_account(request):
    if request.method == 'POST':
        form = SavingsAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SavingsAccountForm()
    return render(request, 'registration/savings_account.html', {'form': form})

def success(request):
    return render(request, 'registration/success.html')
