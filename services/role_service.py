from sqlalchemy.orm import Session
from repository.role_repo import RoleRepository
from schema.role_schema import RoleCreate, RoleUpdate, Role


class RoleService:
    def __init__(self, db: Session):
        self.repository = RoleRepository(db)
        self.validate_roles = [role.value for role in Role]

    def get_all_roles(self):

        return self.repository.get_all()

    def get_role_by_id(self, role_id: str):

        return self.repository.get_by_id(role_id)

    def create_role(self, role_data: RoleCreate):
        
        if role_data.role not in self.validate_roles:
            return "ROLE NOT EXISTS"
        
        return self.repository.create(role_data)

    def update_role(self, role_id: str, role_data: RoleUpdate):
        
        if role_data.role is not None:
            if role_data.role not in self.validate_roles:
                return "ROLE NOT EXISTS"

        return self.repository.update(role_id, role_data)

    def delete_role(self, role_id: str):

        return self.repository.delete(role_id)
    
    def get_all_hr(self):
        return self.repository.get_all_hr()
    
    def get_all_recruiters(self):
        return self.repository.get_all_recruiters()

    def get_all_viewer(self):
        return self.repository.get_all_viewers()
    
    def get_roles_count_by_date(self):
        return self.repository.get_roles_count_by_date()
    
    def get_roles_ranking(self):
        return self.repository.get_roles_ranking()