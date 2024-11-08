import csv
from datetime import date

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            date_new = date.fromisoformat(phone['release_date'])
            phone_model = Phone(name=phone['name'],
                                price=int(phone['price']),
                                image=phone['image'],
                                release_date=date_new,
                                lte_exists=bool(phone['lte_exists']),
                                slug=slugify(phone['name']))
            phone_model.save()

