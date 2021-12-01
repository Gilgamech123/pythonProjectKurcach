from firstapp.views import *
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PageIndex.as_view()),
    path('home.html', PageHome.as_view()),
    path('index.html', PageIndex.as_view()),
    path('registration.html', PageRegistration.as_view()),
    path('login.html', PageLogin.as_view()),
    path('dogovor.html', PageDogovor.as_view()),
    path('home_employeer.html', PageHomeEmployeer.as_view()),
    path('application_for_payment.html/<int:id>', PageApplicationPayment.as_view()),
    path('payment.html/<int:id>', PagePayment.as_view()),
    path('home_admin.html', PageHomeAdmin.as_view()),
    path('registration_employeer.html', PageRegistrationEmployeer.as_view()),
    path('edit_view.html/<int:id>', EditViewPage.as_view()),
    path('edit_customer.html/<int:id>', EditCustomer.as_view()),
    path('edit_employeer.html/<int:id>', EditEmployeer.as_view()),
    path('edit_application.html/<int:id>', EditApplication.as_view()),
    path('add_view.html', AddView.as_view()),
    path('delete_dogovor.html/<int:id>', DeleteDogovor.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)