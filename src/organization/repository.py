from typing import List, Optional
from sqlalchemy.orm import Session

from .schema import OrganizationModel
from db.tables import Organization

class OrganizationRepository:
    def __init__(self, session: Session):
        self.session = session


    def get_all(self) -> List[Optional[OrganizationModel]]:
        return self.session.query(Organization).all()