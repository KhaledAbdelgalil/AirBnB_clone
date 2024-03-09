#!/usr/bin/python3
"""City Module."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for managing city information.

    Attributes:
        state_id (str): The ID of the associated state.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
