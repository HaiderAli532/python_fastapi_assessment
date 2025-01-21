from typing import List, Optional
from user.repository import UserRepository
from sqlalchemy.orm import Session

from user.schema import UserModel


class UserService:
    def __init__(self, session: Session):
        self.repository = UserRepository(session)

    def get_all(self) -> List[Optional[UserModel]]:
        return self.repository.get_all()