import datetime

from django.shortcuts import render
from django.views import View
from .basa import *
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.views.generic import DeleteView

class PageLogin(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context=context)

    def post(self, request):
        request.session["id_admin"] = 0
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
            check_level = check_prava_level(request.session["id_user"])
            check = check_prava(request.session["id_user"])

            if not check:
                if not check_level:
                    return HttpResponseRedirect('home.html')
                else:
                    request.session["id_admin"] = check_level[0].id
                    request.session["priv_user"] = check_level[0].position
                    return HttpResponseRedirect('home_admin.html')
            else:
                request.session["id_employeer"] = check[0].id
                request.session["priv_user"] = check[0].position
                return HttpResponseRedirect('home_employeer.html')

class PageDogovor(View):
    def get(self, request):
        if 'id_user' in request.session.keys():
            infoCustomer = Customer.objects.filter(user_id = request.session["id_user"])
            employeer_list = Employeer.objects.all()
            views_list = TypeOfInsurance.objects.all()
            context = {
                #'infoUser': infoUser,
                'employeer_list': employeer_list,
                'views_list': views_list,
                'infoCustomer': infoCustomer
            }
            return render(request, 'dogovor.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            customer = request.POST.get("customer")
            employeer = request.POST.get("employeer")
            type_view = request.POST.get("type_view")
            time = request.POST.get("time")
            sum_insurance = request.POST.get("sum_insurance")
            add_dogovor(customer, employeer, type_view, time, sum_insurance)
        context = {}
        return HttpResponseRedirect("../home.html")


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

class PageHomeEmployeer(View):
    def get(self, request):
        if 'id_employeer' in request.session.keys() and 'id_user' in request.session.keys():
            information = get_info(request.session['id_user'])
            infoemployeer = get_info_employeer(request.session['id_employeer'])
            infoDogovorEmployeer = get_info_dogovor_employeer(request.session['id_employeer'])
            context = {
                'information': information,
                'infoemployeer': infoemployeer,
                'infoDogovorEmployeer': infoDogovorEmployeer
                }
            return render(request, 'home_employeer.html', context=context)

class PageIndex(View):
    def get(self, request):
        views_list = TypeOfInsurance.objects.all()
        context = {
            'views_list': views_list
        }
        return render(request, 'index.html', context=context)

class PageRegistration(View):
    def get(self, request):
        context = {}
        return render(request, 'registration.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            patronymic = request.POST.get("patronymic")
            login = request.POST.get("login")
            password = request.POST.get("password")
            passport_data = request.POST.get("numpasport")
            snills = request.POST.get("numsnils")
            add_user(name,surname, patronymic, login, password)
            add_customer(passport_data, snills)
        context = {}
        return render(request, 'login.html', context=context)

class PageApplicationPayment(View):
    def get(self, request, id):
        if 'id_user' in request.session.keys():
            rezult_info = get_info_dogovor_2(request.session['id_user'], id)
            context = {
                'rezult_info': rezult_info
            }
        return render(request, 'application_for_payment.html', context=context)

    def post(self, request,id):
        if request.method == 'POST':
            dogovor = request.POST.get("dogovor")
            doctor_opinion = request.FILES['doctor_opinion']
            customer_request = request.POST.get("customer_request")
            add_aplication(dogovor, doctor_opinion,customer_request)
        context = {}
        return HttpResponseRedirect("../home.html")

class PagePayment(View):
    def get(self, request,id):
        if 'id_user' in request.session.keys():
            infodogovor = get_info_dogovor_2(request.session['id_user'], id)
            check_pay = check_payment(id)
            context = {
                'check_pay': check_pay,
                'infodogovor': infodogovor
            }
            return render(request, 'payment.html', context=context)

    def post(self, request, id):
        if request.method == 'POST':
            sum_pay = request.POST.get("sum_pay")
            bank_details = request.POST.get("bank_details")
            add_paymant(id, sum_pay, bank_details)
        context = {}
        return HttpResponseRedirect("../home.html")

class PageHomeAdmin(View):
    def get(self, request):
        if 'id_admin' in request.session.keys() and 'id_user' in request.session.keys():
            information = get_info_user_admin(request.session['id_user'])
            infoadmin = get_info_admin(request.session['id_admin'])
            dogovors_list = Dogovor.objects.all()
            views_list = TypeOfInsurance.objects.all()
            users_list = User.objects.all()
            customers_list = Customer.objects.all()
            employeer_list = Employeer.objects.all()
            aplications_list = ApplicationForPayment.objects.all()
            payment_list = Payment.objects.all()

            context = {
                'information': information,
                'infoadmin': infoadmin,
                'dogovors_list': dogovors_list,
                'views_list': views_list,
                'users_list': users_list,
                'customers_list': customers_list,
                'employeer_list': employeer_list,
                'aplications_list': aplications_list,
                'payment_list': payment_list
                #'infoDogovorEmployeer': infoDogovorEmployeer
            }
        return render(request, 'home_admin.html', context=context)

class PageRegistrationEmployeer(View):
    def get(self, request):
        context = {}
        return render(request, 'registration_employeer.html', context=context)
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            patronymic = request.POST.get("patronymic")
            login = request.POST.get("login")
            password = request.POST.get("password")
            name_position = request.POST.get("position")
            add_user(name,surname, patronymic, login, password)
            add_employeer(name_position)
        context = {}
        return HttpResponseRedirect("../home_admin.html")

class EditViewPage(View):
    def get(self, request, id):
        infoview  = get_info_view(id);
        #data = datetime.datetime(infoview.сontract_time).strptime("d.m.Y")
        context = {
            'infoview': infoview
            #'data': data
            }
        return render(request, 'edit_view.html', context=context)
    def post(self, request, id):
        if request.method == 'POST':
            nameView = request.POST.get("nameView")
            percentage_of_insurance_premium = request.POST.get("percentage_of_insurance_premium")
            сontract_time = request.POST.get("сontract_time")
            edit_view(id, nameView,percentage_of_insurance_premium, сontract_time)
        context = {}
        return HttpResponseRedirect("../home_admin.html")

class EditCustomer(View):
    def get(self, request, id):
        infoUser = get_info_user(id)
        infoCustomer = Customer.objects.all()
        context = {
            'infoUser': infoUser,
            'infoCustomer':infoCustomer
        }
        return render(request, 'edit_customer.html', context=context)

    def post(self, request, id):
        if request.method == 'POST' and 'id_user' in request.session.keys() and 'id_admin' in request.session.keys():
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            patronymic = request.POST.get("patronymic")
            login = request.POST.get("login")
            password = request.POST.get("password")
            passport_data = request.POST.get("numpasport")
            snills = request.POST.get("numsnils")
            edit_user(id, name, surname, patronymic, login, password)
            edit_customer(id, passport_data, snills)
            check_level = check_prava_level(request.session["id_user"])
            print(request.session["id_admin"])
            if  request.session["id_admin"]==0:
                return HttpResponseRedirect("../home.html")
            else:
                return HttpResponseRedirect("../home_admin.html")


class EditEmployeer(View):
    def get(self, request, id):
        infoUser = get_info_user(id)
        context = {
            'infoUser': infoUser
        }
        return render(request, 'edit_employeer.html', context=context)

    def post(self, request, id):
        if request.method == 'POST' :
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            patronymic = request.POST.get("patronymic")
            login = request.POST.get("login")
            password = request.POST.get("password")
            position = request.POST.get("position")
            edit_user(id, name, surname, patronymic, login, password)
            edit_employeer(id, position)
        context = {}
        print(request.session["priv_user"])
        if request.session["priv_user"] == "работник":
            return HttpResponseRedirect('../home_employeer.html')
        else:
            return HttpResponseRedirect('../home_admin.html')

class AddView(View):
    def get(self, request):
        context = {}
        return render(request, 'add_view.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            nameView = request.POST.get("nameView")
            percentage_of_insurance_premium = request.POST.get("percentage_of_insurance_premium")
            сontract_time = request.POST.get("сontract_time")
            add_view(сontract_time, nameView, percentage_of_insurance_premium)
        context = {}
        return HttpResponseRedirect("../home_admin.html")

class EditApplication(View):
    def get(self, request, id):
        info_application = open_info(id)
        context = {
            'info_application': info_application
        }
        return render(request, 'edit_application.html', context=context)
    def post(self, request, id):
        if request.method == 'POST':
            nameView = request.POST.get("rez")
            edit_application(id, nameView)
        context = {}
        return HttpResponseRedirect("../home_admin.html")

class DeleteDogovor(View):
    def get(self, request, id):
        delete = Dogovor.objects.get(id=id)
        delete.delete()
        return HttpResponseRedirect("../home.html")

class DeleteDogovor1(View):
    def get(self, request, id):
        delete = Dogovor.objects.get(id=id)
        delete.delete()
        return HttpResponseRedirect("../home_employeer.html")

class DeleteDogovor2(View):
    def get(self, request, id):
        delete = TypeOfInsurance.objects.get(id=id)
        delete.delete()
        return HttpResponseRedirect("../home_admin.html")

class DeleteDogovor3(View):
    def get(self, request, id):
        delete = Employeer.objects.get(id=id)
        delete.delete()
        return HttpResponseRedirect("../home_admin.html")

class DeleteDogovor4(View):
    def get(self, request, id):
        delete = Customer.objects.get(id=id)
        delete.delete()
        return HttpResponseRedirect("../home_admin.html")

class DeleteDogovor5(View):
    def get(self, request, id):
        delete = ApplicationForPayment.objects.get(id=id)
        delete.delete()
        return HttpResponseRedirect("../home_admin.html")

class DeleteDogovor6(View):
    def get(self, request, id):
        delete = Payment.objects.get(id=id)
        delete.delete()
        return HttpResponseRedirect("../home_admin.html")