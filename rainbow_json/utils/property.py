class Property:
    """class to mark a json property"""    
    def __init__(self, typename: type, property_name: str) -> None:
        self.name = property_name
        self.type = typename