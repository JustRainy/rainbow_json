from rainbow_json.utils.property import Property
from typing import Callable



def json_property(property_name: str, type: type, is_iterable: bool = False, generics: list[type]|None = None):
    def transform(_: Callable) -> Property:
        """change an attribute into an instance of Property for converter to recognize"""
        return Property(typename = type, property_name = property_name, is_iterable = is_iterable, generics = generics)
    return transform