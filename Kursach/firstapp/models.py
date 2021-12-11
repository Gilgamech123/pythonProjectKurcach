from django.db import models
from django.utils import timezone

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    passport_data = models.CharField(max_length=150)
    snills = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.name

class Employeer(models.Model):
    position = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.name

class Admin(models.Model):
    position = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.name

class TypeOfInsurance(models.Model):
    сontract_time = models.DateTimeField()
    Name_view = models.CharField(max_length=150)
    percentage_of_insurance_premium = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.Name_view

class Dogovor(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employeer = models.ForeignKey(Employeer, on_delete=models.CASCADE)
    type_view = models.ForeignKey(TypeOfInsurance, on_delete=models.CASCADE)
    time = models.DateField(default=timezone.now)
    sum_insurance = models.DecimalField(max_digits=20, decimal_places=2)

class ApplicationForPayment(models.Model):
    dogovor = models.ForeignKey(Dogovor, on_delete=models.CASCADE, verbose_name="Номер договора")
    doctor_opinion = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Заключение врача")
    customer_request = models.TextField(blank=True, verbose_name="Заявление клиента")
    approved = models.BooleanField(default=True, verbose_name="Одобрено")

class Payment(models.Model):
    applicationForPayment = models.ForeignKey(ApplicationForPayment, on_delete=models.CASCADE, verbose_name="Номер заявки")
    sum_pay = models.DecimalField(max_digits=20, decimal_places=2)
    transfer_account  = models.CharField(max_length=150)