from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Apartment, Booking
from .forms import FreeForm
from Hotel.brone.free_apartment import check_free_apartment

#представление списка комнат
def ApartmentList(request):
    apartment = Apartment.objects.all()[0]
    apartment_types = dict(apartment.APARTMENT_TYPES)
    apartment_description = dict(apartment.APARTMENT_DESCRIPTIONS)
    print("типы: ", apartment_types)
    apartment_values = apartment_types.values()
    print("значения: ", apartment_values)
    apartment_list = []
    for type in apartment_types:
        apart = apartment_types.get(type)
        apart_url = reverse('Hotel:ApartmentView', kwargs={'type': type})
        apart_description = apartment_description.get(type)
        apartment_list.append((apart, apart_url, apart_description))
    context = {
        "apartment_list": apartment_list,
    }
    return render(request, 'apartmentList.html', context)

class BookingList(ListView):
    model = Booking
    template_name = "booking_list.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
        return booking_list

#детальное представление одной комнаты
class ApartmentView(View):
    def get(self, request, *args, **kwargs):
        apart_type = self.kwargs.get('type', None)
        form = FreeForm()
        apartment_list = Apartment.objects.filter(type=apart_type)
        if len(apartment_list) > 0:
            apartment = apartment_list[0]
            apartment_type = dict(apartment.APARTMENT_TYPES).get(apartment.type, None)
            apartment_description = dict(apartment.APARTMENT_DESCRIPTIONS).get(apartment.type, None)
            context = {
                'apartment_type': apartment_type,
                'form': form,
                'apartment_description': apartment_description
            }
            return render(request, 'appartmentView.html', context)
        else:
            return HttpResponse('Не существует такой комнаты')

    def post(self, request, *args, **kwargs):
        apart_type = self.kwargs.get('type', None)
        apartment_list = Apartment.objects.filter(type=apart_type)
        form = FreeForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
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
        
class CancelBooking(DeleteView):
    model = Booking
    template_name = 'booking_cancel.html'
    success_url = reverse_lazy('Hotel:BookingList')

def mainPage(request):
    return render(request, "main_page.html")

# class Loginout(View):


# class BookingView(FormView):
#     form_class = FreeForm
#     template_name = "free_form.html"

#     def form_valid(self, form):
#         data = form.cleaned_data
#         apartment_list = Apartment.objects.filter(type=data["room_type"])
#         free_rooms = [room for room in apartment_list if check_free_apartment(room, data['date_reg'], data['date_end'])]
#         if len(free_rooms) > 0:
#             room = free_rooms[0]
#             booking = Booking.objects.create(
#                 user = self.request.user,
#                 room = room,
#                 date_reg = data['date_reg'],
#                 date_end = data['date_end']
#             )
#             booking.save()
#             return HttpResponse(booking)
#         else:
#             return HttpResponse('Категория комнат забронирована. Попробуйте другую')