
from typing import List
from fastapi import APIRouter, Depends
# from db.dbsettings import get_session
from sqlalchemy.orm import Session

from .service import OrganizationService
from .schema import OrganizationModel
from db.dbsettings import get_session

organization_router = APIRouter()
 
@organization_router.get(
    "/organization",
    tags=["Organization"],
    summary="Get All Organization",
    description="Get all application Organization data",
    response_model=List[OrganizationModel]
)
def get_all_organization(session: Session = Depends(get_session)):
    return OrganizationService(session).get_all()