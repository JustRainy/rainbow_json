from abc import ABC, abstractmethod
from rainbow_json.utils.property import Property
import inspect



class JObject(ABC):
    """mark a available class"""
    @abstractmethod
    def __init__(self) -> None:
        self._index = {i[0]: i[1] for i in inspect.getmembers(self) if isinstance(i[1], Property)}