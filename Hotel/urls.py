from django.urls import path
from .views import ApartmentList, BookingList, ApartmentView, CancelBooking

app_name = 'Hotel'

urlpatterns = [
    path('apartment_list/', ApartmentList, name='ApartmentList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    # path('book/', BookingView.as_view(), name='BookingView'),
    path('apartment/<type>', ApartmentView.as_view(), name='ApartmentView'),
    path('booking/cancel/<pk>', CancelBooking.as_view(), name='CancelBooking')
]