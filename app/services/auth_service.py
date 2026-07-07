from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.password import verify_password
from app.utils.jwt import create_access_token


class AuthService:

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str,
    ):

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if user is None:
            raise Exception("Invalid email or password")

        if not verify_password(
            password,
            user.password,
        ):
            raise Exception("Invalid email or password")

        token = create_access_token(
            {
                "sub": user.email
            }
        )

        return token, user