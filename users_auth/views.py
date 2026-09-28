from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users_auth.forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_view')

    if request.method == 'POST':
        form_data = LoginForm(request, data=request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            if user:
                login(request, user)
                messages.success(request, 'User Logged-in Successfully.')
                return redirect('dashboard_view')
        else:
            messages.warning(request, 'Invalid credentials.')
    else:
        form_data = LoginForm()

    return render(request, 'login.html', {'form_data': form_data})


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully.')
    return redirect('login_view')