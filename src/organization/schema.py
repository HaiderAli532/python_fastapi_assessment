from typing import Optional

from pydantic import BaseModel, Field


class OrganizationModel(BaseModel):
    id: Optional[int] = Field(description="User Id")
    name: Optional[str] = Field(description="User name")
    contact_info: Optional[str] = Field(description="Contact info of client")
    user_id: Optional[int] = Field(description="Client Id which makes company")
