#!/usr/bin/python3
"""Review module."""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class representing a review

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
