from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
from cleaner.forms import UploadFileForm
from cleaner.cleaner import clean_data

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            # Automatically log in the user after registration
            login(request,user)
            return redirect('dashboard')
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    form = UploadFileForm()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            options = {
                "handle_missing": form.cleaned_data["handle_missing"],
                "apply_iqr": form.cleaned_data["apply_iqr"],
                "encode_labels": form.cleaned_data["encode_labels"],
                "drop_dupes": form.cleaned_data["drop_dupes"],
            }
            df, report = clean_data(request.FILES["csv_file"], options)
            request.session["cleaned_csv"] = df.to_csv(index=False)
            request.session["report"] = report
            request.session["preview"] = df.head(6).to_html(classes="table table-bordered")  if len(df) >= 6 else df
            
            return redirect("results")
    return render(request, "accounts/dashboard.html", {"form": form})
@login_required
def results_view(request):
    table = request.session.get("preview", None)
    report = request.session.get("report", None)
    return render(request, "accounts/results.html", {
        "table": table,
        "report": report,
    })


