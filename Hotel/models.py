from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

class Apartment(models.Model):
    APARTMENT_TYPES = (('STD', 'STANDART'), ('BDR', 'BEDROOM'), ('SPR', 'SUPERIOR'), ('DLX', 'DELUXE'))
    number = models.IntegerField()
    type = models.CharField(max_length=3, choices=APARTMENT_TYPES)
    count_beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.number} комната - {self.type} с {self.count_beds} спальными местами для {self.capacity} гостей"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    date_reg = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return f"{self.user} зарезервировал {self.room} в период с {self.date_reg} до {self.date_end}"

    def get_apartment_type(self):
        return dict(Apartment.APARTMENT_TYPES).get(self.room.type)
    
    def cancel_booking(self):
        return reverse_lazy('Hotel:CancelBooking', args=[self.pk, ])
