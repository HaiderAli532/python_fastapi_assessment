from typing import Optional

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: Optional[int] = Field(description="User Id")
    name: Optional[str] = Field(description="User name")
    email: Optional[str] = Field(description="User Email")
    password: Optional[str] = Field(description="User Password")
    role: Optional[str] = Field(description="User Role (Freelance or Client)")