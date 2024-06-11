
from django.core.management.base import BaseCommand
import requests

from core.models import Planet, Film, People

class Command(BaseCommand):
    help = 'Seed data'

    def get(self, path:str):
        self._base_url = 'https://swapi.dev/api/'
        response = requests.get(f'{self._base_url}{path}').json()
        data = response['results']
        has_next = response['next'] != None

        while has_next:
            response = requests.get(response['next']).json()
            data.extend(response['results'])
            has_next = response['next'] != None
        return data

    def cleand_external_ids_ref(self, list_url):
        return list(map(lambda x: int(x.split('/')[-2]), list_url))


    def load_planets(self):
        self.stderr.write('Load planets')
        data = self.get('planets')
        for planet in data:
            Planet.objects.get_or_create(
                name=planet['name'],
                rotation_period=planet['rotation_period'],
                orbital_period=planet['orbital_period'],
                diameter=planet['diameter'],
                climate=planet['climate'],
                gravity=planet['gravity'],
                terrain=planet['terrain'],
                surface_water=planet['surface_water'],
                population=planet['population'],
                external_reference=int(planet['url'].split('/')[-2])
            )

    def load_films(self):
        self.stderr.write('Load films...')
        data = self.get('films')
        for film in data:
            Film.objects.get_or_create(
                title=film['title'],
                episode_id=film['episode_id'],
                opening_crawl=film['opening_crawl'],
                director=film['director'],
                producer=film['producer'],
                release_date=film['release_date'],
                external_reference=int(film['url'].split('/')[-2])
            )

    def load_people(self):
        self.stderr.write('Load people...')
        data = self.get('people')
        for people in data:
            object_people, _ = People.objects.get_or_create(
                name=people['name'],
                height=people['height'],
                mass=people['mass'],
                hair_color=people['hair_color'],
                gender=people['gender'],
                dob=people['birth_year']
            )
            object_people.homeworld = Planet.objects.get(external_reference=int(people['homeworld'].split('/')[-2]))
            films = self.cleand_external_ids_ref(people['films'])
            object_people.films.set(Film.objects.filter(external_reference__in=films))
            object_people.save()

    def handle(self, *args, **options):
        self.stderr.write('Init process...')

        try:
            self.load_planets()
            self.load_films()
            self.load_people()
            self.stderr.write('Finish process...')
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))

