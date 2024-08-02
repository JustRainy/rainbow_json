from typing import Callable


class Property:
    """class to mark a json property"""    
    def __init__(self, typename: type, property_name: str, is_iterable: bool, generics: list[type]) -> None:
        self.name = property_name
        self.type = typename
        self.iterable = is_iterable
        self.generics = generics

    def __str__(self) -> str:
        return (self.name, self.type)


def json_property(property_name: str, type: type, is_iterable: bool = False, generics: list[type] = []):
    def transform(_: Callable) -> Property:
        """change an attribute into an instance of Property for converter to recognize"""
        return Property(typename = type, property_name = property_name, is_iterable = is_iterable, generics = generics)
    return transform