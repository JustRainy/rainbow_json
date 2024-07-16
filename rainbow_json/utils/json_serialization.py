from rainbow_json.exception import NotJObjectError
from rainbow_json.bases import JObject
from json import loads, dumps
from typing import Any



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
                name = tmp[i].name
                tp = tmp[i].type
                if(tmp[i].iterable):
                    if(isinstance(json_dict.get(name), list)):
                        obj.__dict__[i] = []
                        if(issubclass(tp, JObject)):
                            for j in json_dict.get(name):
                                if(isinstance(j, dict)):
                                    obj.__dict__[i].append(JsonSerializer.diserialize(tp, dumps(j)))
                                else:
                                    raise TypeError(f"{i} doesn't match the type of the json property {name} , do you mean {type(j)} instead?")
                        else:
                            for j in json_dict.get(name):
                                if(tp == type(j) or tp == Any or tp == object):
                                    obj.__dict__[i].append(j)
                                else:
                                    raise TypeError(f"{i} doesn't match the type of the json property {name} , do you mean {type(j)} instead?")
                elif(issubclass(tp, JObject)):
                    obj.__dict__[i] = JsonSerializer.diserialize(tp, dumps(json_dict.get(name)))
                elif(tp == type(json_dict.get(name)) or tp == Any or tp == object):
                    obj.__dict__[i] = json_dict.get(name)
                else:
                    raise TypeError(f"the attribute {i} doesn't match the type of the json property {name} , do you mean {type(json_dict.get(name))} instead?")
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
                elif isinstance(tmp[key], tmp1[key].type):
                    json[tmp1[key].name] = tmp[key]
                else:
                    raise TypeError(f"the attribute {key} doesn't match the type of the json property {tmp1[key].name}")
            
            return dumps(json)

