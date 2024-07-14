from rainbow_json.base import JObject
from rainbow_json.exception import NotJObjectError
from rainbow_json.utils.property import Property
from json import loads, dumps
import inspect



class JsonSerializer:
    @staticmethod
    def diserialize(_type: type, json: str) -> object:
        """Change a json str into a Python object"""
        json_dict: dict = loads(json)
        if _type == dict:
            return json_dict
        else:
            #try:
                if issubclass(_type, JObject):
                    obj = _type()
                    for i in inspect.getmembers(obj):
                        if not isinstance(i[1], Property):
                            continue
                        else:
                            if(i[1].iterable):
                                #TODO: iterable
                                ...
                            else:
                                if(issubclass(i[1].type, JObject)):
                                    obj.__dict__[i[0].lstrip("_")] = JsonSerializer.diserialize(i[1].type, dumps(json_dict.get(i[1].name)))
                                else:
                                    if(i[1].type == type(json_dict.get(i[1].name))):
                                        obj.__dict__[i[0].lstrip("_")] = json_dict.get(i[1].name)
                                    else:
                                        raise TypeError("this attribute doesn't match the type of the json value")
                    return obj
                else:
                    raise NotJObjectError("this class is not a json object")

            #except Exception as e:
                #raise e

    @staticmethod
    def serialize(obj: object) -> str:
        if(not isinstance(obj, JObject)):
            raise NotJObjectError("this class is not a json object")
        else:
            json = {}
            for key in (d := obj.__dict__):
                if(isinstance(d[key], JObject)):
                    json[getattr(obj, f"_{key}").name] = loads(JsonSerializer.serialize(d[key]))
                else:
                    json[getattr(obj, f"_{key}").name] = d[key]
            
            return dumps(json)

