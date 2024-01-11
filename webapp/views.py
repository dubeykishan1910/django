from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateRecordForm, updateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record
# Create your views here.


# home page
def home(request):
    # return HttpResponse("hell of first")
    return render(request, 'webapp/index.html')

# Register a user
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)

# Login a user
def my_login(request):
    form = LoginForm()
     
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")

    context = {'form':form}
    return render(request, 'webapp/login.html',context=context)




# Dashboard
# get 
@login_required(login_url = 'login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}
    return render(request, 'webapp/dashboard.html', context=context)


# create a record 
@login_required(login_url = 'login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("deshboard")

    context = {'form':form}







# user logout 

def user_logout(request):
    auth.logout(request)

    return redirect("login")
















# attendance_app/views.py


# from django.shortcuts import render, redirect
# from .models import AttendanceRecord
# from .forms import AttendanceForm

# def take_attendance(request):
#     records = []  # to store temporary records in the loop

#     if request.method == 'POST':
#         form = AttendanceForm(request.POST)
#         if form.is_valid():
#             record = form.save(commit=False)
#             records.append(record)
#         else:
#             return render(request, 'attendance_app/take_attendance.html', {'form': form})

#     else:
#         form = AttendanceForm()

#     return render(request, 'attendance_app/take_attendance.html', {'form': form, 'records': records})

# def attendance_summary(request):
#     if request.method == 'POST':
#         records = []
#         total_working_hours = timedelta()
#         total_breaks = timedelta()

#         for record_data in request.POST.getlist('records'):
#             entry_time_str, exit_time_str = record_data.split('-')
#             entry_time = datetime.strptime(entry_time_str, "%H:%M")
#             exit_time = datetime.strptime(exit_time_str, "%H:%M")
            
#             records.append({'entry_time': entry_time, 'exit_time': exit_time})

#             if total_working_hours:
#                 break_duration = entry_time - total_working_hours[-1]['exit_time']
#                 total_breaks += max(break_duration, timedelta())  # Ensure positive break time

#             total_working_hours.append({'entry_time': entry_time, 'exit_time': exit_time})

#         return render(request, 'attendance_app/attendance_summary.html', {'records': records, 'total_working_hours': total_working_hours, 'total_breaks': total_breaks})

#     return redirect('take_attendance')
