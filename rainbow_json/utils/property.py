class Property:
    """class to mark a json property"""    
    def __init__(self, typename: type, property_name: str, is_iterable: bool) -> None:
        self.name = property_name
        self.type = typename
        self.iterable = is_iterable