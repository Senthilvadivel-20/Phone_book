import phonenumbers
from phonenumbers import geocoder,carrier,timezone


def number(num):
    ph=phonenumbers.parse("+91"+num)

    land_mark=geocoder.description_for_number(ph,'en')

    sim=carrier.name_for_number(ph,'en')

    time_zone=timezone.time_zones_for_number(ph)

    return land_mark,sim,time_zone



