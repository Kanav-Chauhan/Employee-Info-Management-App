from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
import requests
from dotenv import load_dotenv
import os
load_dotenv() 

# 🔹 Weather API Function
def get_weather(city='Mohali'):
    api_key = os.getenv('OPENWEATHER_API_KEY')  # replace with your key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    r = requests.get(url).json()
    if 'main' in r:
        return {'city': city, 'temp': r['main']['temp'], 'desc': r['weather'][0]['description']}
    return {'city': city, 'temp': 'N/A', 'desc': 'Unavailable'}

# 🔹 Dashboard
def dashboard(request):
    weather = get_weather()
    count = Employee.objects.count()
    return render(request, 'employees/dashboard.html', {'weather': weather, 'count': count})

# 🔹 List
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# 🔹 Add
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form, 'title': 'Add Employee'})

# 🔹 Edit
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form, 'title': 'Edit Employee'})

# 🔹 Delete
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/confirm_delete.html', {'employee': employee})
