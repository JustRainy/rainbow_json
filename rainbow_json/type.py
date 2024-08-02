from rainbow_json.base import JTypes
from typing import override



class __JList(JTypes):
    @override
    def __init__(self) -> None:
        self.type = list
    
    @override
    def __getitem__(self, T: type|JTypes):
        self.generic = T
        return self


class __JDict(JTypes):
    @override
    def __init__(self) -> None:
        self.type = dict

    @override
    def __getitem__(self, T: tuple[type, type|JTypes]):
        self.generic = T[1]
        self.generic_k = T[0]
        return self


List = __JList()
Dict = __JDict()