# Cities coordinates

cities_coordinates is a python package that helps to identify cities' coordinations arround the 
### Installation

See [pypi](https://pypi.org/project/cities-coordinates/), [Github](https://github.com/sofzer/cities_coordinates)

cities_coordinates python and pip to be installed.

In order to install the plugin, run the following command:

```sh
pip install cities_coordinates
```

#### Usage 
For now this package has two basical methods the first one `get_city()` returns the city coordinations using a city name and its country code, the second `get_country_cities` returns all of the cities that belongs to the given country code.
```sh
from cities_coordinates import CityCoordinator
c=CityCoordinator()
c.get_city(city_name="Jena",country_code_iso="DE")
# {'country_iso_code': 'DE', 'city_name': 'Jena', 'location': {'lat': '50.92878', 'lon': '11.5899'}}

c.get_country_cities(country_code_iso="DE")
#[
# {'country_iso_code': 'DE', 'city_name': 'Lenningen', 'location': {'lat': '48.55048', 'lon': '9.47674'}}, 
# {'country_iso_code': 'DE', 'city_name': 'Lobbach', 'location': {'lat': '49.37519', 'lon': '8.88884'}}, 
# {'country_iso_code': 'DE', 'city_name': 'Sachsenheim', 'location': {'lat': '48.96', 'lon': '9.06472'}} 
#...]
```

# I'll be happy if you like this helpful package and feel free contribute to it
