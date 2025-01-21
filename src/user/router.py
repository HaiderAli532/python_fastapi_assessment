
from typing import List
from fastapi import APIRouter, Depends
# from db.dbsettings import get_session
from sqlalchemy.orm import Session

from user.service import UserService
from .schema import UserModel
from db.dbsettings import get_session

user_router = APIRouter()
 
@user_router.get(
    "/users",
    tags=["User"],
    summary="Get All Users",
    description="Get all application users data",
    response_model=List[UserModel]
)
def get_users(session: Session = Depends(get_session)):
    user_service = UserService(session)
    return user_service.get_all()