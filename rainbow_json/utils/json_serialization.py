from rainbow_json.base import JObject
from rainbow_json.exception import NotJObjectError
from rainbow_json.utils.property import Property
from json import loads
import inspect



class JsonSerializer:
    @staticmethod
    def diserialize(_type: type, json: str) -> object:
        json_dict: dict = loads(json)
        if _type == dict:
            return json_dict
        else:
            #try:
                if isinstance(_type(), JObject):
                    obj = _type()
                    for i in inspect.getmembers(obj, inspect.ismethod):
                        if not isinstance(i[1], Property):
                            continue
                        else:
                            if(isinstance(i[1].type, list)):
                                ...
                            else:
                                if(JObject in i.type.__bases__):
                                    JsonSerializer.diserialize(i)
                                else:
                                    obj.__dict__[key] = json_dict.get(key)
                    return obj
                else:
                    raise NotJObjectError("this class is not a json object")

            #except Exception as e:
                #raise e