from rainbow_json.utils import json_property, JsonSerializer
from rainbow_json.bases import JObject
from typing import Any
import json as js



with open("example.json") as f:
    json = f.read()

class Char(JObject):
    @json_property("hobby", str)
    def hobby(self): ...

    @json_property("idol", str)
    def ikun(self): ...


class Student(JObject):
    @json_property("detail", Char, is_iterable = True)
    def detail(self): ...

    @json_property("class", int)
    def cls(self): ...

    @json_property("name", Any)
    def name(self): ...
a: Student = JsonSerializer.diserialize(Student, json)
#print(a.detail[0].ikun)
#a.detail[2].hobby = "rap"
#a.cls = 1
#b = JsonSerializer.serialize(a)
#print(b)
print(a._index)
print(a.__dict__)
b = {
    "class": 1, 
    "detail": [
        {
            "hobby": "chang", 
            "idol": "i"
        }, 
        {
            "hobby": "tiao", 
            "idol": "k"
        }, 
        {
            "hobby": "rap", 
            "idol": "u"
        }, 
        {
            "hobby": "basketball", 
            "idol": "n"
        }
        ], 
    "name": "mike"
}
with open("example.json", "w") as f:
    f.write(JsonSerializer.serialize(b))
#with open("example.json", "w") as f:
    #f.write(b)
print(a.detail[0].ikun)