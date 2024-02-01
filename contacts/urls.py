from django.urls import path

from contacts.views import AddressesAPIView, EmailsAPIView, PhoneNumbersAPIView

urlpatterns = [
    path('phone_number/api', PhoneNumbersAPIView.as_view()),
    path('address/api', AddressesAPIView.as_view()),
    path('email/api', EmailsAPIView.as_view()),
]
