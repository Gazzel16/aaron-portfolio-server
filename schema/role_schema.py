from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class Role(str, Enum):
    hr = "hr"
    viewer = "viewer"
    recruiter = "recruiter"
    

class RoleResponse(BaseModel):
    id: str
    name: str
    role: str
    created_at: datetime
    updated_at: datetime

class RoleCountByDateResponse(BaseModel):
    date: str
    count: int
    
class RoleRankingResponse(BaseModel):
    role: str
    count: int

class RoleCreate(BaseModel):
    name: str
    role: str
    
class RoleUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None

class RoleDelete(BaseModel):
    id: str

    