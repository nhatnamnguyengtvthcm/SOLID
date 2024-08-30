from persistence_service import PersistenceService
from order import Order


class OrderPersistenceService (PersistenceService[Order]):
    _orders: dict[int, Order] = {}

    def save(self, entity: Order):
        self._orders[entity.get_id()] = entity

    def delete(self, entity: Order):
        del self._orders[entity.id]


    def find_by_id(self, id: float) -> Order:
        return self._orders[id] if self._orders.get(id) else None




# order_persistence = OrderPersistenceService()


# order = Order()
# order.set_id(1)
# order.set_order_place_on('2021-09-01')
# order.set_total_value(100)
# order_persistence.save(order)