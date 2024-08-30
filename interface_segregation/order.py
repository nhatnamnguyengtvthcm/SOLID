from datetime import datetime
from entity import Entity


class Order(Entity):
    
    _order_place_on: datetime
    _total_value: float

    def get_order_place_on(self):
        return self._order_place_on

    def set_order_place_on(self, order_place_on: datetime):
        self._order_place_on = order_place_on

    def get_total_value(self):
        return self._total_value

    def set_total_value(self, total_value: float):
        self._total_value = total_value
