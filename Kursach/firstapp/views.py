from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from .basa import *
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import *
from .forms import *


class PageLogin(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context=context)

    def post(self, request):
        login = request.POST.get("login")
        password = request.POST.get("password")
        users = autoriz(login, password)
        if not users:
            context = {
                "message": "Введен не правильный пароль или логин"
            }
            return render(request, 'login.html', context=context)
        else:

            request.session["id_user"] = users[0].id
            check = check_prava(request.session["id_user"])
            emp = get_info_serch(check)
            if not emp:

                return HttpResponseRedirect('home.html')
            else:
                return HttpResponseRedirect('home_emploeer.html')

class PageDogovor(View):
    def get(self, request):
        if request.method == 'POST':
            form = AddDogovor(request.POST)
            if form.is_valid():
                new_dogovor = form.save(commit=False)
                new_dogovor.save()
        else:
            form = AddDogovor()
        context = {

            'form': form
        }
        return render(request, 'dogovor.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            form = AddDogovor(request.POST)
            if form.is_valid():
                new_dogovor = form.save(commit=False)
                new_dogovor.save()
        else:
            form = AddDogovor()
        context = {
            'form': form
        }
        return render(request, 'home.html', context=context)


class PageHome(View):
    def get(self, request):
        if 'id_user' in request.session.keys():
            tasks = get_material(request.session['id_user'])
            information = get_info(request.session['id_user'])
            ifnodogovor1 = get_count_dogovor()
            ifnodogovor = get_info_dogovor(request.session['id_user'])
            context = {
                'tasks': tasks,
                'information': information,
                'ifnodogovor': ifnodogovor,
                'ifnodogovor1': ifnodogovor1

            }
        return render(request, 'home.html', context=context)

class PageHomeEmpoyeer(View):
    def get(self, request):
        context = {}
        return render(request, 'home_emploeer.html', context=context)

class PageIndex(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)


class PageRegistration(View):
    def get(self, request):
        if request.method == 'POST':
            form = AddUserForm(request.POST)
            form2 = AddCustomerForm(request.POST)
            if form.is_valid() and form2.is_valid():
                new_user = form.save(commit=False)
                new_user.save()
                new_user2 = form2.save(commit=False)
                new_user2.save()

        else:
            form = AddUserForm()
            form2 = AddCustomerForm()
            context = {
                'form': form,
                'form2': form2
            }
        return render(request, 'registration.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            form = AddUserForm(request.POST)
            form2 = AddCustomerForm(request.POST)
            if form.is_valid() and form2.is_valid():
                new_user = form.save(commit=False)
                new_user.save()
                new_user2 = form2.save(commit=False)
                new_user2.save()

        else:
            form = AddUserForm()
            form2 = AddCustomerForm()
        context = {
            'form': form,
            'form2': form2

        }
        return render(request, 'login.html', context=context)




