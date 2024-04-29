from datetime import timezone

from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .models import Book, Issue


@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def about_view(request):
    return render(request, 'about_us.html')


def contact_view(request):
    return render(request, 'contact_us.html')


def index(request):
    book = Book.objects.filter(is_published=True)
    context = {'book': book}
    return render(request, 'index.html', context)


def user_login(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,password=password)
            print('user = ', user)
            if user:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('index')
            else:
                messages.error(request, 'Logged in Fail')
    return render(request, 'login.html', context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration.html"


@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to maintain user's session
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required(login_url='/login')
def profile(request):
    # Assuming you have a OneToOneField relationship between User and Profile models
    profile = request.user

    return render(request, 'profile.html', {'profile': profile})


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookIssueForm()
    context = {
        "book": book,
        "form": form
    }
    return render(request, 'book_details.html', context)


@login_required(login_url='/login')
def book_issue(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookIssueForm(request.POST)
    if form.is_valid():
        return_date = form.cleaned_data.get('return_date')
        email = form.cleaned_data.get('email')
        address = form.cleaned_data.get('address')
        phone = form.cleaned_data.get('phone')

        book_issue_create = Issue.objects.create(
            user=request.user,
            book=book,
            issued=True,
            return_date=return_date,
            email=email,
            address=address,
            mobile=phone
        )
        print("book_issue_create", book_issue_create)
        return redirect('my_book_issue_list')


@login_required(login_url='/login')
def my_book_issue_list(request):
    user = request.user
    issues = Issue.objects.filter(user=user)
    context = {'issues': issues}
    return render(request, 'issue.html', context)


@login_required(login_url='/login')
def update_profile(request):
    form = ProfileUpdateForm()
    context = {
        'user': request.user,
        'form': form
    }
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')

            user = User.objects.get(pk=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return redirect('profile')

    return render(request, 'update_profile.html', context)

