const data_people = [
    {
        "id": "14ab16be-2164-4ddc-b668-eeb106867063",
        "name": "Raymus Antilles",
        "height": "188",
        "mass": "79",
        "hair_color": "brown",
        "gender": "male",
        "dob": "unknown",
        "img": null,
        "homeworld": "Alderaan",
        "films": [
            {
                "title": "Revenge of the Sith",
                "release_date": "2005-05-19"
            },
            {
                "title": "A New Hope",
                "release_date": "1977-05-25"
            }
        ]
    },
    {
        "id": "adbae7cc-fb51-47ca-811c-1e669da5bfc5",
        "name": "Tarfful",
        "height": "234",
        "mass": "136",
        "hair_color": "brown",
        "gender": "male",
        "dob": "unknown",
        "img": null,
        "homeworld": "Kashyyyk",
        "films": [
            {
                "title": "Revenge of the Sith",
                "release_date": "2005-05-19"
            }
        ]
    },
    {
        "id": "6b3846b4-d50e-4bf1-a28c-1d7de107be12",
        "name": "Cliegg Lars",
        "height": "183",
        "mass": "unknown",
        "hair_color": "brown",
        "gender": "male",
        "dob": "82BBY",
        "img": null,
        "homeworld": "Tatooine",
        "films": [
            {
                "title": "Attack of the Clones",
                "release_date": "2002-05-16"
            }
        ]
    },
    {
        "id": "6d2509fb-d2bb-4257-99ff-e0676de16ad7",
        "name": "Ric Olié",
        "height": "183",
        "mass": "unknown",
        "hair_color": "brown",
        "gender": "male",
        "dob": "unknown",
        "img": null,
        "homeworld": "Naboo",
        "films": [
            {
                "title": "The Phantom Menace",
                "release_date": "1999-05-19"
            }
        ]
    },
    {
        "id": "dd59f3f3-cc16-44e2-9490-4f8254de7b17",
        "name": "Qui-Gon Jinn",
        "height": "193",
        "mass": "89",
        "hair_color": "brown",
        "gender": "male",
        "dob": "92BBY",
        "img": null,
        "homeworld": "unknown",
        "films": [
            {
                "title": "The Phantom Menace",
                "release_date": "1999-05-19"
            }
        ]
    },
    {
        "id": "deef393b-b611-4aec-9f05-305249d250ee",
        "name": "Wicket Systri Warrick",
        "height": "88",
        "mass": "20",
        "hair_color": "brown",
        "gender": "male",
        "dob": "8BBY",
        "img": null,
        "homeworld": "Endor",
        "films": [
            {
                "title": "Return of the Jedi",
                "release_date": "1983-05-25"
            }
        ]
    },
    {
        "id": "47e95667-d8b0-4a1f-8ec7-fd69446d52e0",
        "name": "Arvel Crynyd",
        "height": "unknown",
        "mass": "unknown",
        "hair_color": "brown",
        "gender": "male",
        "dob": "unknown",
        "img": null,
        "homeworld": "unknown",
        "films": [
            {
                "title": "Return of the Jedi",
                "release_date": "1983-05-25"
            }
        ]
    },
    {
        "id": "36254746-6fcb-4309-b0fa-990562a5e08c",
        "name": "Jek Tono Porkins",
        "height": "180",
        "mass": "110",
        "hair_color": "brown",
        "gender": "male",
        "dob": "unknown",
        "img": null,
        "homeworld": "Bestine IV",
        "films": [
            {
                "title": "A New Hope",
                "release_date": "1977-05-25"
            }
        ]
    }
]

const Home = () => {
    return (
        <div className="bg-white">
          <div className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
            <h2 className="text-5xl font-bold tracking-tight text-gray-900">StarWars UI</h2>
            <div className="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
              {data_people.map((people) => (
                <div key={people.id} className="group relative">
                  <div className="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 border border-indigo-900 lg:aspect-none group-hover:opacity-75 lg:h-80">
                    <img
                      src={'https://blog.spoongraphics.co.uk/wp-content/uploads/2012/star-wars/29.jpg'}
                      alt={people.name}
                      className="h-full w-full object-cover object-center lg:h-full lg:w-full"
                    />
                  </div>
                  <div className="mt-4 flex justify-between">
                    <div>
                      <h2 className="text-3lx text-gray-700">
                        <a href={people.href}>
                          <span aria-hidden="true" className="absolute inset-0" />
                          {people.name}
                        </a>
                      </h2>
                      <p className="mt-1 text-sm text-gray-500">{people.gender}</p>
                    </div>
                    <p className="text-sm font-medium text-gray-900">{people.homeworld}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )
}


export default Home