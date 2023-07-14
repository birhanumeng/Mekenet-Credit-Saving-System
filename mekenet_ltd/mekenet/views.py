from django.shortcuts import render, redirect

from .models import CustomerInfo, CustomerLoan, CustomerSaving
from .forms import CustomerSavingForm


def home(request):
    """ Creating home page """
    return render(request, 'home.html', {})


def customers(request):
    """ Create a customers information page """
    customers = CustomerInfo.objects.all()
    context = {'customers': customers}
    return render(request, 'customers.html', context)


def customer(request, key):
    """ Selecting a single customer """
    customer = CustomerInfo.objects.get(id=key)
    context = {'customer': customer}
    return render(request, customers.html, customer)


def saving(request):
    """ Create a customers saving information page """
    saves = CustomerSaving.objects.all()
    context = {'saves': saves}
    return render(request, 'saving.html', context)


def loans(request):
    """ Create a customers loans information page """
    loans = CustomerLoan.objects.all()
    context = {'loans': loans}
    return render(request, 'loans.html', context)


def createSaving(request):
    """ Creating new saving page """
    form = CustomerSavingForm()
    if request.method == "POST":
        form = CustomerSavingForm(request.POST)
        if form.is_valid():
            form.save()
            #save_obj = form.save(commit=False)
            #save_id = save_obj.id
            #customer = CustomerSaving.objects.get(id=save_id)
            
            #customer.balance = cutomer.balance + save_obj.compulsary + save_obj.voluntary
            #customer.maker = 

            return redirect('saves')
    context = {'form': form}
    return render(request, 'create_saving.html', context)


def updateSaving(request, key):
    """ Update saving page """
    save = CustomerSaving.objects.get(id=key)
    form = CustomerSavingForm(instance=save)

    if request.method == "POST":
        form = CustomerSavingForm(request.POST, instance=save)
        if form.is_valid():
            form.save()
            return redirect('saves')
    context = {'form': form}
    return render(request, 'create_saving.html', context)


def deleteSaving(request, key):
    """ Delete saving page """
    save = CustomerSaving.objects.get(id=key)
    
    if request.method == "POST":
        save.delete()
        return redirect('saves')
    context = {'object': save}
    return render(request, 'delete_template.html', context)


def createLoan(request):
    """ Create loan registration form """
    context = {}
    return render(request, 'loan_form.html', context)