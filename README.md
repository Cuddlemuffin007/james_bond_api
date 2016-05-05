# james_bond_api
An API for EON-production James Bond films, based on swapi

accepted resource names are characters, vehicles, gadgets, movies, bond-actors
as a subset of characters, character types are also accepted - allies, villains, henchmen, bond-girls

all resources can be accessed via /api/<resource_name>/ routes
ex. /api/characters/
returns a paginated list of all (major) characters in the Bond films, 10 results per page

appending a querystring ?page=2 will return that specific page
ex. /api/vehicles/?page=3
returns page 3 of vehicles

optionally add an integer to retrieve a specific entry /api/<resource_name>/:id
ex.
/api/characters/1
returns character #1, James Bond himself
