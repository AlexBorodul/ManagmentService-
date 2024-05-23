import datetime
from Hotel.models import Apartment, Booking

def check_free_apartment(apartment, date_reg, date_end):
    list_of_booking = Booking.objects.filter(room=apartment)
    list_of_free_rooms = [True if (booking.date_reg > date_end or booking.date_end < date_reg) else False for booking in list_of_booking]
    return all(list_of_free_rooms)
