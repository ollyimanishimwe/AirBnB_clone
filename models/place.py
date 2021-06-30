#!/usr/bin/python3
"""
User class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    Attributes:
    city_id: string - empty string or the City.id
    user_id: string - empty string or the User.id
    name: string - place name
    description: string - place description
    number_rooms: integer - number of rooms in place
    number_bathrooms: integer - number of bathrooms in place
    max_guest: integer - place's max guest capacity
    price_by_night: integer - place's price by night
    latitude: float - place's latitute
    longitude: float - place's longitude
    amenity_ids: list of string - empty list or the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
