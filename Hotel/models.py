from django.db import models
from django.conf import settings

class Apartment(models.Model):
    APARTMENT_TYPES = (('STD', 'STANDART'), ('BDR', 'BEDROOM'), ('SPR', 'SUPERIOR'), ('STD', 'STUDIO'), ('DLX', 'DELUXE'))
    number = models.IntegerField()
    type = models.CharField(max_length=3, choices=APARTMENT_TYPES)
    count_beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.number} room - {self.type} with {self.count_beds} beds for {self.capacity} guests"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    date_reg = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return f"{self.user} booked {self.room} from {self.date_reg} to {self.date_end}"

