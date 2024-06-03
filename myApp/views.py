from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Students
from .forms import StudentForm

# Display all students on the index page
def index(request):
    students = Students.objects.all()
    return render(request, 'myApp/index.html', {
        'students': students
    })

# View a specific student, using student_number as the primary key
def view_student(request, student_number):
    student = Students.objects.get(student_number=student_number)
    return HttpResponseRedirect(reverse('index'))

# Add a new student through a form
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the form to create a new student record
            form.save()
            return render(request, 'myApp/add.html', {
                'form': StudentForm(),  # Provide a fresh form for new entries
                'success': True  # Pass a success flag to the template
            })
    else:
        form = StudentForm()  # Initialize a blank form for GET requests

    return render(request, 'myApp/add.html', {
        'form': form  # Pass the form with potential validation errors back to the template
    })

# Edit an existing student record
def edit(request, student_number):
    student = Students.objects.get(student_number=student_number)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'myApp/edit.html', { # Redirect to the edit page with a success flag
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)

    return render(request, 'myApp/edit.html', {
        'form': form,
        'student': student
    })
#delete a student record
def delete(request, student_number):
    student = Students.objects.get(student_number=student_number)
    student.delete()
    return HttpResponseRedirect(reverse('index'))
  