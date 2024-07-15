from rainbow_json.utils import json_property, JsonSerializer
from rainbow_json.bases import JObject



with open("example.json") as f:
    json = f.read()

class Char(JObject):
    def __init__(self) -> None: super().__init__()

    @json_property("hobby", str)
    def hobby(self): ...

    @json_property("idol", str)
    def ikun(self): ...


class Student(JObject):
    def __init__(self) -> None: super().__init__()

    @json_property("detail", Char)
    def detail(self): ...

    @json_property("class", int)
    def cls(self): ...

    @json_property("name", str)
    def name(self): ...

a: Student = JsonSerializer.diserialize(Student, json)
print(a.detail.hobby)
a.detail.hobby = "rap"
a.cls = 114514
b = JsonSerializer.serialize(a)
print(b)
print(a._index)
with open("example.json", "w") as f:
    f.write(b)