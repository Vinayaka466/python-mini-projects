from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html')

from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, UpdateAgeForm

# List students
def index(request):
    students = Student.objects.filter(course="Database Systems")
    return render(request, 'index.html', {'students': students})

# Add a new student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# Update the student's age
def update_age(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = UpdateAgeForm(request.POST)
        if form.is_valid():
            student.age = form.cleaned_data['age']
            student.save()
            return redirect('index')
    else:
        form = UpdateAgeForm(initial={'age': student.age})
    return render(request, 'update_age.html', {'form': form, 'student': student})
