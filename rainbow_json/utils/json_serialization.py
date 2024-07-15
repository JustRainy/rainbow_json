from rainbow_json.bases import JObject
from rainbow_json.exception import NotJObjectError
from json import loads, dumps



class JsonSerializer:
    @staticmethod
    def diserialize(_type: type, json: str) -> object:
        """Change a json str into a Python object"""
        json_dict: dict = loads(json)
        if _type == dict:
            return json_dict
        elif issubclass(_type, JObject):
            obj = _type()
            for i in (tmp := obj._index):
                if(tmp[i].iterable):
                    # TODO: iterable
                        ...
                elif(issubclass(tmp[i].type, JObject)):
                    obj.__dict__[i] = JsonSerializer.diserialize(tmp[i].type, dumps(json_dict.get(tmp[i].name)))
                elif(tmp[i].type == type(json_dict.get(tmp[i].name))):
                    obj.__dict__[i] = json_dict.get(tmp[i].name)
                else:
                    raise TypeError("this attribute doesn't match the type of the json value")
            return obj
        else:
            raise NotJObjectError("this class is not a json object")

    @staticmethod
    def serialize(obj: object) -> str:
        if(not isinstance(obj, JObject)):
            raise NotJObjectError("this class is not a json object")
        else:
            json = {}
            tmp = obj.__dict__
            for key in (tmp1 := obj._index):
                if(isinstance(tmp[key], JObject)):
                    json[tmp1[key].name] = loads(JsonSerializer.serialize(tmp[key]))
                else:
                    json[tmp1[key].name] = tmp[key]
            
            return dumps(json)

