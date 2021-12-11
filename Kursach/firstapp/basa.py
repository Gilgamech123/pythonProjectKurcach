from .models import *
import datetime

def get_material(user_id):
    materials = Customer.objects.filter(user=user_id)
    return materials

def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users

def get_info(user_id):
    info = User.objects.filter(id=user_id)
    return info

def get_info_customer(user_id):
    info = Customer.objects.filter(user=user_id)
    return info

def get_info_dogovor(user_id):

    info_dogovor = Dogovor.objects.filter(customer=user_id)
    return info_dogovor

def get_info_dogovor_2(user_id, id):

    info_dogovor = Dogovor.objects.filter(customer=user_id, id = id)
    return info_dogovor

def get_count_dogovor():
    count = Dogovor.objects.all().count()
    return count

def get_name():
    name = Employeer.objects.all()
    return name

def get_view():
    view = TypeOfInsurance.objects.all()
    return view

def get_info_serch(employeer):
    info_employeer = Employeer.objects.filter(id=employeer)
    return info_employeer
def get_cost(name_view):
    getCost = TypeOfInsurance.objects.filter(Name_view = name_view)
    return getCost

def serch_id_user(name, surname, patronymic):
    rezult = User.objects.filter(name = name, surname = surname, patronymic = patronymic)
    return rezult

def serch_id_customer(idUser):
    rezult = Customer.objects.filter(id = idUser)
    return rezult


def check_prava(user_id):
    rez = Employeer.objects.filter(user=user_id)
    return rez

def check_prava_level(user_id):
    rez = Admin.objects.filter(user=user_id)
    return rez

def get_info_employeer(employeer_id):
    info = Employeer.objects.filter(id = employeer_id)
    return info

def get_info_dogovor_employeer(employeer_id):
    info_dogovor = Dogovor.objects.filter(employeer=employeer_id)
    return info_dogovor

def check_apporoved_true(application_id, rez):
    anser = ApplicationForPayment(id =application_id, approved = rez)
    return anser


def add_user(name,surname, patronymic, login, password):
    add_User = User(name = name,surname = surname, patronymic = patronymic , login = login, password = password)
    add_User.save()

def add_customer(passport_data, snills):
    add_Customer = Customer(passport_data = passport_data, snills = snills)
    add_Customer.user = User.objects.order_by('-id').first()
    add_Customer.save()

def add_employeer(name_position):
    add_Employeer = Employeer(position = name_position)
    add_Employeer.user = User.objects.order_by('-id').first()
    add_Employeer.save()

def add_dogovor(customer, employeer, type_view, time, sum_insurance):
    info = Customer.objects.filter(user__name=customer)
    info2 = Employeer.objects.filter(user__name=employeer)
    info3 = TypeOfInsurance.objects.filter(Name_view=type_view)
    add_Dogovor = Dogovor(customer = info[0], employeer = info2[0],  type_view= info3[0], time = time, sum_insurance = sum_insurance)
    add_Dogovor.save()

def get_info_user_admin(user_id):
    info = User.objects.filter(id=user_id)
    return info

def get_info_admin(admin_id):
    info = Admin.objects.filter(id=admin_id)
    return info


def check_payment(id):
    rez= ApplicationForPayment.objects.filter(dogovor = id)

    return rez

def add_paymant(id, sum_pay, bank_details):
    add_basa = Payment(sum_pay = sum_pay, transfer_account = bank_details)
    add_basa.applicationForPayment = ApplicationForPayment.objects.order_by('id').get(id = id)
    add_basa.save()

def add_aplication(dogovor, doctor_opinion,customer_request):
    info = Dogovor.objects.filter(id = dogovor)
    add_Aplication = ApplicationForPayment(dogovor = info[0], doctor_opinion = doctor_opinion, customer_request = customer_request)
    add_Aplication.save()

def add_view(сontract_time, nameView, percentage_of_insurance_premium):
    add_View = TypeOfInsurance(сontract_time = сontract_time, Name_view = nameView, percentage_of_insurance_premium = percentage_of_insurance_premium )
    add_View.save()

def get_info_view(id):
    rez= TypeOfInsurance.objects.filter(id = id)
    return rez

def edit_view(id, nameView,percentage_of_insurance_premium, сontract_time):
    edit_view = TypeOfInsurance.objects.get(id = id)
    edit_view.сontract_time = сontract_time
    edit_view.Name_view = nameView
    edit_view.percentage_of_insurance_premium = percentage_of_insurance_premium
    edit_view.save()

def get_info_user(id):
    rez = User.objects.filter(id = id)
    return rez
def get_info_user_customer(id):
    rez = Customer.objects.filter(id = id)
    return rez

def edit_user(id, name, surname, patronymic, login, password):
    edit_user = User.objects.get(id=id)
    edit_user.name = name
    edit_user.surname = surname
    edit_user.patronymic = patronymic
    edit_user.login = login
    edit_user.password = password
    edit_user.save()

def edit_customer(id, passport_data, snills):
    edit_customer = Customer.objects.get(user=id)
    edit_customer.snills = snills
    edit_customer.passport_data = passport_data
    edit_customer.save()

def edit_employeer(id, position):
    edit_employeer = Employeer.objects.get(user=id)
    edit_employeer.position = position
    edit_employeer.save()

def edit_application(id, nameView):
    edit_application = ApplicationForPayment.objects.get(id=id)
    edit_application.approved = nameView
    edit_application.save()

def open_info(id):
    rez = ApplicationForPayment.objects.filter(id=id)
    return rez

def getdata():
    data = datetime.datetime.now()
    return data