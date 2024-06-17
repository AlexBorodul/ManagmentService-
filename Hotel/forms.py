from django import forms

class FreeForm(forms.Form):
    # APARTMENT_TYPES = (('STD', 'STANDART'), ('BDR', 'BEDROOM'), ('SPR', 'SUPERIOR'), ('STD', 'STUDIO'), ('DLX', 'DELUXE'))
    # room_type = forms.ChoiceField(choices=APARTMENT_TYPES, required=True)
    date_reg = forms.DateTimeField(required=True, input_formats=["%d-%m-%YT%H:%M", ])
    date_end = forms.DateTimeField(required=True, input_formats=["%d-%m-%YT%H:%M", ])
    