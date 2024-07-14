from rainbow_json.utils import json_property, JsonSerializer
from rainbow_json.base import JObject



with open("1.json") as f:
    json = f.read()

class Char(JObject):
    def __init__(self) -> None:...

    @json_property("hobby", str)
    def _hobby(self): ...

    @json_property("idol", str)
    def _ikun(self): ...


class Student(JObject):
    def __init__(self) -> None:...

    @json_property("detail", Char)
    def _detail(self): ...

    @json_property("class", str)
    def _cls(self): ...

    @json_property("name", str)
    def _name(self): ...

a: Student = JsonSerializer.diserialize(Student, json)
print(a.detail.hobby)
a.detail.hobby = "rap"
a.cls = "2"
b = JsonSerializer.serialize(a)
print(b)
with open("1.json", "w") as f:
    f.write(b)