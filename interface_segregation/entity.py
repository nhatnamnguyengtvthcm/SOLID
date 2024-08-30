from abc import ABC, abstractmethod

class Entity(ABC):

    _id: float
       
    def get_id(self):
        return self._id
    
    def set_id(self, id: float):  
        self._id = id
  