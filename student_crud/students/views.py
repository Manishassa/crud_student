from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student

# Home View
def home(request):
    if request.user.is_authenticated:
        return redirect('student_list')
    else:
        return redirect('signup')

# Authentication Views
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('student_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'students/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('student_list')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('student_list')
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('home')

# Create your views here.
# READ - List Students
@login_required
def student_list(request):
    students=Student.objects.all()
    return render(request,'students/list.html',{'students':students})


# CREATE - Add Student


# render() = "Show this page right here." (Stay on same page)

# redirect() = "Go to another page (browser makes a new request)."

@login_required
def create_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # age = request.POST.get('age')
        Branch = request.POST.get('Branch')

        Student.objects.create(name=name,email=email,Branch=Branch)
        return redirect('student_list')
    return render(request,'students/create.html')


# UPDATE - Edit Student

@login_required
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email'] #branch = request.POST['Branch']
        # student.age = request.POST['age']
        student.Branch = request.POST['Branch']
        student.save()
        return redirect('student_list')
    return render(request, 'students/update.html', {'student': student})

# DELETE - Remove Student
@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


