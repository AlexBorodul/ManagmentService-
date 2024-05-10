from django.db import models

class Apartment(models.Model):
    APARTMENT_TYPES = (('STD', 'STANDART'), ('BDR', 'BEDROOM'), ('SPR', 'SUPERIOR'), ('STD', 'STUDIO'), ('DLX', 'DELUXE'))
    number = models.IntegerField()
    type = models.CharField(max_length=3, choices=APARTMENT_TYPES)
    count_beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.number} room - {self.type} with {self.count_beds} beds for {self.capacity} guests"
