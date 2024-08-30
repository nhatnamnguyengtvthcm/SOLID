from datetime import datetime
from entity import Entity
from user import User
from persistence_service import PersistenceService


class UserPersistenceService(PersistenceService[User]):
    
    _users: dict[int, User] = {}

    def save(self, entity: User):
        self._users[entity.get_id()] = entity
        
    def find_by_id(self, id: float) -> User:
        return self._users[id] if self._users.get(id) else None
    
    def find_by_name(self, name: str) -> list[User]:
        return [user for user in self._users.values() if name in user.name]

    def delete(self, entity: User):
        del self.users[entity.id]


user = User()
user.set_id(1)
user.set_name('John Doe')
# user.set_last_login(datetime.now())
user.set_last_login("2021-09-01")

user_persistence = UserPersistenceService()
user_persistence.save(user)
print(user_persistence.find_by_id(1).get_name())
print(user_persistence.find_by_id(1).get_last_login())