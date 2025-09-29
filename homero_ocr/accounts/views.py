from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, "dashboard.html")
