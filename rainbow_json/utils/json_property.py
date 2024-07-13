from rainbow_json.utils.property import Property



def json_property(property_name: str, type: type):
    def transform(attr) -> Property:
            """change an attribute into an instance of Property for converter to recognize"""
            return Property(typename = type, property_name = property_name)
    return transform