from rainbow_json.exception import NotJObjectError
from rainbow_json.bases import JObject
from json import loads, dumps
from typing import Any



class JsonSerializer:
    @staticmethod
    def diserialize(_type: type, json: str, generics: list[type] = []) -> object:
        """Change a json str into a Python object"""
        json_obj = loads(json)
        json_type = type(json_obj)
        obj = json_obj
        if _type == json_type:
            if(any(generics)):
                if(json_type == list):
                    obj = []
                    match len(generics):
                        case 1:
                            for i in json_obj:
                                obj.append(JsonSerializer.diserialize(generics[0], dumps(i)))
                        case _:
                            num = 0
                            for i in json_obj:
                                obj.append(JsonSerializer.diserialize(generics[num], dumps(i)))
                                num += 1
                elif(json_type == dict):
                    obj = {}
                    match len(generics):
                        case 1:
                            for i in json_obj:
                                obj[i] = (JsonSerializer.diserialize(generics[0], dumps(json_obj[i])))
                        case _:
                            num = 0
                            for i in json_obj:
                                obj[i] = (JsonSerializer.diserialize(generics[num], dumps(json_obj[i])))
                                num += 1
        elif _type == object or _type == Any:...
        elif issubclass(_type, JObject):
            obj = _type()
            # judge if _type equals to target json
            assert len(obj._index) == len(json_obj), f"length of {_type.__name__} doesn't match that of the json str, check if you've ignored some property"

            for i in (tmp := obj._index):
                nm, tp, gs = tmp[i].name, tmp[i].type, tmp[i].generics
                if json_type == dict:
                    if(tmp[i].iterable):
                        if(isinstance(json_obj.get(nm), list)):
                            obj.__dict__[i] = []
                            for j in json_obj.get(nm):
                                obj.__dict__[i].append(JsonSerializer.diserialize(tp, dumps(j), gs))
                        else:
                            raise TypeError
                    else:
                        obj.__dict__[i] = JsonSerializer.diserialize(tp, dumps(json_obj.get(nm)), gs)
                else:
                    raise TypeError

        else:
            raise NotJObjectError("this class is not a json object")
        
        return obj

    @staticmethod
    def serialize(obj: object) -> str:
        if(isinstance(obj, JObject)):
            json = {}
            tmp = obj.__dict__
            for key in (tmp1 := obj._index):
                if(isinstance(tmp[key], JObject)):
                    json[tmp1[key].name] = loads(JsonSerializer.serialize(tmp[key]))
                elif isinstance(tmp[key], tmp1[key].type):
                    json[tmp1[key].name] = tmp[key]
                else:
                    raise TypeError(f"the attribute {key} doesn't match the type of the json property {tmp1[key].name}")
            
            return dumps(json, indent = 4)
        elif(isinstance(obj, dict)):
            return dumps(obj, indent = 4)
        else:
            raise NotJObjectError("this class is not a json object")