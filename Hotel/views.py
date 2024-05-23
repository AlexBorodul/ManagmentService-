from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Apartment, Booking
from .forms import FreeForm
from Hotel.brone.free_apartment import check_free_apartment


class ApartmentList(ListView):
    model = Apartment

class BookingList(ListView):
    model = Booking


class BookingView(FormView):
    form_class = FreeForm
    template_name = "free_form.html"

    def form_valid(self, form):
        data = form.cleaned_data
        apartment_list = Apartment.objects.filter(type=data["room_type"])
        free_rooms = [room for room in apartment_list if check_free_apartment(room, data['date_reg'], data['date_end'])]
        if len(free_rooms) > 0:
            room = free_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                date_reg = data['date_reg'],
                date_end = data['date_end']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('Категория комнат забронирована. Попробуйте другую')