from rainbow_json.exception.error import NotJObjectError
from rainbow_json.base import JObject
from json import loads, dumps
from typing import Any



class JsonSerializer:
    @classmethod
    def diserialize(cls, T: type, json: str, iterable: bool = False) -> object:
        """Change a json str into a Python object"""
        json_obj = loads(json)
        json_type = type(json_obj)
        obj = json_obj
        if(not(iterable)):
            if T == json_type or T == Any or T == object:
                obj = json_obj
            elif(issubclass(T, JObject)):
                obj = T()
                assert len((index := obj._index)) == len(json_obj), f"length of {T.__name__} doesn't match that of the json str, check if you've ignored some property"

                if(json_type == dict):
                    for key in index:
                        nm, tp, it = index[key].name, index[key].type, index[key].iterable
                        obj.__dict__[key] = cls.diserialize(tp, dumps(json_obj.get(nm)), it)
                else:
                    raise
            else:
                raise NotJObjectError("this class is not a json object")
        else:
            if(json_type == dict):
                obj = {}
                for key in json_obj:
                    obj[key] = cls.diserialize(T, dumps(json_obj[key]))
            elif(json_type == list):
                obj = []
                for item in json_obj:
                    obj.append(cls.diserialize(T, dumps(item)))
            else:
                raise
        
        return obj

    @classmethod
    def serialize(cls, obj: object) -> str:
        if(isinstance(obj, JObject)):
            json = {}
            tmp = obj.__dict__
            for key in (tmp1 := obj._index):
                if(isinstance(tmp[key], JObject)):
                    json[tmp1[key].name] = loads(cls.serialize(tmp[key]))
                elif isinstance(tmp[key], tmp1[key].type):
                    json[tmp1[key].name] = tmp[key]
                else:
                    raise TypeError(f"the attribute {key} doesn't match the type of the json property {tmp1[key].name}")
            
            return dumps(json, indent = 4)
        elif(isinstance(obj, dict)):
            return dumps(obj, indent = 4)
        else:
            raise NotJObjectError("this class is not a json object")
        
    @classmethod
    def __format_type(cls, T):
        ...