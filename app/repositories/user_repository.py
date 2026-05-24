from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate

class UserRepository:

    @staticmethod
    def create(db: Session, user_data: UserCreate):
        new_user = User(**user_data.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def get_all(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def update(db: Session, user_id: int, user_data):
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return None

        for key, value in user_data.model_dump().items():
            setattr(user, key, value)

        db.commit()

        db.refresh(user)

        return user

    @staticmethod
    def delete(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            return None

        db.delete(user)
        db.commit()

        return user