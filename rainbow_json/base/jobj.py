from abc import ABC, abstractmethod



class JObject(ABC):
    """mark a available class"""
    @abstractmethod
    def __init__(self) -> None:
        ...