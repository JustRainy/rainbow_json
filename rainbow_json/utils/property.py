class Property:
    """class to mark a json property"""    
    def __init__(self, typename: type, property_name: str, is_iterable: bool, generics: list[type]) -> None:
        self.name = property_name
        self.type = typename
        self.iterable = is_iterable
        self.generics = generics

    def __str__(self) -> str:
        return (self.name, self.type)