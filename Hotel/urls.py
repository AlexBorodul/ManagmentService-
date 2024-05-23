from django.urls import path
from .views import ApartmentList, BookingList, BookingView

app_name = 'Hotel'

urlpatterns = [
    path('apartment_list/', ApartmentList.as_view(), name='ApartmentList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView')
]