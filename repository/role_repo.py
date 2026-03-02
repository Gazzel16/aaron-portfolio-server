from sqlalchemy.orm import Session
from model.role_model import Role
from schema.role_schema import RoleCreate, RoleUpdate
from typing import List, Optional
from sqlalchemy import func, desc

class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Role]:

        return self.db.query(Role).all()

    def get_by_id(self, role_id: str) -> Optional[Role]:

        return self.db.query(Role).filter(Role.id == role_id).first()

    def create(self, role_data: RoleCreate) -> Role:

        db_role = Role(**role_data.model_dump())
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role

    def update(self, role_id: str, role_data: RoleUpdate) -> Optional[Role]:

        db_role = self.get_by_id(role_id)
        if not db_role:
            return None

        # exclude_unset=True is KEY: it only gives us fields the user actually sent
        update_data = role_data.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(db_role, key, value)

        self.db.commit()
        self.db.refresh(db_role)
        return db_role

    def delete(self, role_id: str) -> bool:

        db_role = self.get_by_id(role_id)
        if db_role:
            self.db.delete(db_role)
            self.db.commit()
            return True
        return False
    
    def get_all_hr(self) -> List[Role]:
        """Fetch all users with the 'hr' role"""
        return self.db.query(Role).filter(Role.role == "hr").all()

    def get_all_viewers(self) -> List[Role]:
        """Fetch all users with the 'viewer' role"""
        return self.db.query(Role).filter(Role.role == "viewer").all()

    def get_all_recruiters(self) -> List[Role]:
        """Fetch all users with the 'recruiter' role"""
        return self.db.query(Role).filter(Role.role == "recruiter").all()
    
    def get_roles_count_by_date(self):
        """
        Returns a list of dictionaries with:
        - date
        - count of roles created on that date
        Useful for line charts.
        """
        results = (
            self.db.query(
                func.date(Role.created_at).label("date"),
                func.count(Role.id).label("count")
            )
            .group_by(func.date(Role.created_at))
            .order_by(func.date(Role.created_at))
            .all()
        )

        # Convert to list of dicts
        return [{"date": r.date.isoformat(), "count": r.count} for r in results]
    
    def get_roles_ranking(self):
        """
        Returns roles ordered by the number of occurrences (most picked first).
        Example output:
        [
            {"role": "hr", "count": 10},
            {"role": "viewer", "count": 7},
            {"role": "recruiter", "count": 3},
        ]
        """
        results = (
            self.db.query(
                Role.role,
                func.count(Role.id).label("count")
            )
            .group_by(Role.role)
            .order_by(desc("count"))
            .all()
        )

        return [{"role": r.role, "count": r.count} for r in results]