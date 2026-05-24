from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate

class UserService:

    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        existing_user = UserRepository.get_by_email(
            db,
            user_data.email
        )

        if existing_user:

            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        if len(user_data.password) < 6:

            raise HTTPException(
                status_code=400,
                detail="Password must contain at least 6 characters"
            )

        return UserRepository.create(db, user_data)

    @staticmethod
    def list_users(db: Session):

        return UserRepository.get_all(db)

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        user = UserRepository.get_by_id(db, user_id)

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user