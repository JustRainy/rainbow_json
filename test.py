from rainbow_json.utils import json_property, JsonSerializer
from rainbow_json.bases import JObject
from typing import Any
import time



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

    @json_property("friends", Char, is_iterable = True)
    def e(self): ...
t = time.perf_counter()
a: Student = JsonSerializer.diserialize(Student, json)
print(f"cost: {time.perf_counter() - t: .8f} s")
#print(a.detail[0].ikun)
#a.detail[2].hobby = "rap"
#a.cls = 1
#b = JsonSerializer.serialize(a)
#print(b)
print(a._index)
print(a.__dict__)
#b = {
    #"class": 1, 
    #"detail": [
 #
#with open("example.json", "w") as f:
    #f.write(JsonSerializer.serialize(b))
#with open("example.json", "w") as f:
    #f.write(b)
print(a.detail[0].ikun)
print(a.e[0].hobby)