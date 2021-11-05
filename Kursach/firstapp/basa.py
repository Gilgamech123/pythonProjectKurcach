from .models import *


def get_material(user_id):
    materials = Customer.objects.filter(user=user_id)
    return materials


def autoriz(login, password):
    users = User.objects.filter(login=login, password=password)
    return users


def get_info(user_id):
    info = User.objects.filter(id=user_id)
    return info


def get_info_dogovor(user_id):

    info_dogovor = Dogovor.objects.filter(customer=user_id)
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

def add_dogovor(idCust, employeer, nameView, summ):
    a_user = Customer.objects.filter(id=idCust)
    a_dog = Dogovor(customer = idCust, employeer = employeer,  type_view= nameView, sum_insurance = summ )
    a_dog.save()

def check_prava(user_id):
    rez = Employeer.objects.filter(id=user_id)
    return rez