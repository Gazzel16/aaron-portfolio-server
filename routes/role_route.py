from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schema.role_schema import (
    RoleResponse,
    RoleCreate, 
    RoleUpdate,
    RoleCountByDateResponse,
    RoleRankingResponse
    )
from controller.role_controller import RoleController

router = APIRouter(
    tags=["Roles"]
)

@router.get("/", response_model=List[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    """Fetch all roles from the database."""
    controller = RoleController(db)
    return controller.get_all()

@router.get("/hr", response_model=List[RoleResponse])
def get_all_hr(db: Session = Depends(get_db)):
    controller = RoleController(db)
    return controller.get_all_hr()

@router.get("/recruiters", response_model=List[RoleResponse])   
def get_all_recruiters(db: Session = Depends(get_db)):
    controller = RoleController(db)
    return controller.get_all_recruiters()

@router.get("/viewers", response_model=List[RoleResponse])
def get_all_viewers(db: Session = Depends(get_db)):
    controller = RoleController(db)
    return controller.get_all_viewer()

@router.get("/count-by-date", response_model=List[RoleCountByDateResponse])
def get_roles_count_by_date(db: Session = Depends(get_db)):
    controller = RoleController(db)
    return controller.get_roles_count_by_date()

@router.get("/role-rankings", response_model=List[RoleRankingResponse])
def get_roles_ranking(db: Session = Depends(get_db)):
    controller = RoleController(db)
    return controller.get_roles_ranking()

@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: str, db: Session = Depends(get_db)):
    """Fetch a single role by UUID."""
    controller = RoleController(db)
    return controller.get_one(role_id)

@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(role_data: RoleCreate, db: Session = Depends(get_db)):
    """Create a new role entry."""
    controller = RoleController(db)
    return controller.create(role_data)

@router.patch("/{role_id}", response_model=RoleResponse)
def update_role(role_id: str, role_data: RoleUpdate, db: Session = Depends(get_db)):
    """Update role details partially."""
    controller = RoleController(db)
    return controller.update(role_id, role_data)

@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(role_id: str, db: Session = Depends(get_db)):
    """Remove a role from the database."""
    controller = RoleController(db)
    return controller.delete(role_id)

