from typing import List, Optional
from sqlalchemy.orm import Session

from user.schema import UserModel
from db.tables import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session


    def get_all(self) -> List[Optional[UserModel]]:
        users = self.session.query(User).all()
        return users