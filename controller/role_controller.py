from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from services.role_service import RoleService
from schema.role_schema import RoleCreate, RoleUpdate

class RoleController:
    def __init__(self, db: Session):
        self.service = RoleService(db)

    def get_all(self):
        return self.service.get_all_roles()

    def get_one(self, role_id: str):
        role = self.service.get_role_by_id(role_id)
        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Role not found"
            )
        return role

    def create(self, role_data: RoleCreate):
        new_role = self.service.create_role(role_data)
        if not new_role:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Role type already exists"
            )
        return new_role

    def update(self, role_id: str, role_data: RoleUpdate):
        updated_role = self.service.update_role(role_id, role_data)
        if not updated_role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Role not found"
            )
        return updated_role

    def delete(self, role_id: str):
        success = self.service.delete_role(role_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Role not found"
            )
        return None # Usually paired with a 204 No Content in the route
    
    def get_all_hr(self):
        role = self.service.get_all_hr()
        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Role not found"
            )
            
        return role
    
    def get_all_recruiters(self):
        role = self.service.get_all_recruiters()
        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Role not found"
            )
        return role

    def get_all_viewer(self):
        role = self.service.get_all_viewer()
        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Role not found"
            )
        return role
    
    def get_roles_count_by_date(self):
        role = self.service.get_roles_count_by_date()
        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Not found"
            )
        return role
    
    def get_roles_ranking(self):
        role = self.service.get_roles_ranking()
        if not role:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Not found"
            )
        return role
    
    