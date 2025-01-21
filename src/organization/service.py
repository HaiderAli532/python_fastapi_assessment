from typing import List, Optional
from .repository import OrganizationRepository
from sqlalchemy.orm import Session

from .schema import OrganizationModel


class OrganizationService:
    def __init__(self, session: Session):
        self.repository = OrganizationRepository(session)

    def get_all(self) -> List[Optional[OrganizationModel]]:
        return self.repository.get_all()