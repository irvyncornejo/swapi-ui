from ..models import People, Film, Planet

class SetUp:
    def _run(self) -> None:
        self.planet = Planet.objects.create(
            name="Tatooine",
            rotation_period="23",
            orbital_period="304",
            diameter="10465",
            climate="arid",
            gravity="1 standard",
            terrain="desert",
            surface_water="1",
            population="200000",
            external_reference=1
        )

        self.film = Film.objects.create(
            title="A New Hope",
            episode_id="4",
            opening_crawl="It is a period of civil war.\nRebel spaceships, striking\nfrom a hidden base, have won\ntheir first victory against\neventual opposition...",
            director="George Lucas",
            producer="Rick McCallum",
            release_date="1977-05-25",
            external_reference=4
        )

        self.people = People.objects.create(
            name="Luke Skywalker",
            height="172",
            mass="77",
            hair_color="blond",
            dob="19BBY",
            gender="male",
            img=''
        )
        self.people.homeworld = self.planet
        self.people.films.set([self.film])
        self.people.save()