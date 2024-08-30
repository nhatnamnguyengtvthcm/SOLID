from abc import ABC, abstractmethod

from entity import Entity
from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from entity import Entity

T = TypeVar('T', bound=Entity)

class PersistenceService((ABC), Generic[T]):

    @abstractmethod
    def save(self, entity: T):
        pass

    @abstractmethod
    def delete(self, entity: T):
        pass

    @abstractmethod
    def find_by_id(self, id: float) -> T:
        pass
    
    @abstractmethod
    def find_by_name(self, name: str) -> list[T]:
        pass

