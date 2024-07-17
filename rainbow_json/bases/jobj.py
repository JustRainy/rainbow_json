from abc import ABC, abstractmethod
from rainbow_json.utils.property import Property
import inspect



class JObject(ABC):
    """mark a available class"""
    def __init__(self, **kwds) -> None:
        self._index = {i[0]: i[1] for i in inspect.getmembers(self) if isinstance(i[1], Property)}
        if set(kwds.keys()) <= set(self._index.keys()):
            self.__dict__.update(kwds)
        else:
            raise AttributeError(f"{self.__class__.__name__} object doesn't have such property, maybe you should check you spelling")