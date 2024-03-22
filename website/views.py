from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Employee
from .forms import AddEmployeeForm

# Create your views here.

def home(request):
    employee_list = Employee.objects.all()
    return render(request, 'website/home.html', {'emp_list' : employee_list})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You were authenticated and logged in successfully.')
            return redirect('home')
        else:
            messages.success(request, 'Login failed, try again!')
            return redirect('login')
    else:
        return render(request, 'website/home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def employee_view(request,pk):
    if request.user.is_authenticated:
        current_employee = Employee.objects.get(pk=pk)
        return render(request, 'website/employee.html', {'emp' : current_employee})
    else:
        return redirect('home')
    
def delete(request, pk):
    if request.user.is_authenticated:
        current_employee = Employee.objects.get(pk=pk)
        current_employee.delete()
        messages.success(request, 'Employee record deleted successfully')
        return redirect('home')
    else:
        messages.success(request, 'You have to be logged in to delete a record')
        return redirect('home') 

def add_employee(request):
    form = AddEmployeeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'A new employee record was successfully added')
                return redirect('home')
        return render(request, 'website/add_employee.html', {'form' : form})
    else:
        messages.success(request, 'You have to be logged in to create a new employee record')
        return redirect('home')
    
def update_employee(request, pk):
    current_employee = Employee.objects.get(pk=pk)
    form = AddEmployeeForm(request.POST or None, instance=current_employee)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'Employee record was successfully updated')
                return redirect('home')
        return render(request, 'website/update_employee.html', {'form' : form})
    else:
        messages.success(request, 'You have to be logged in to update an employee record')
        return redirect('home')