import strawberry
from strawberry.types import Info

from app.database.database import SessionLocal
from app.graphql.types import AuthResponse, UserType
from app.models.user import User
from app.services.auth_service import AuthService
from app.utils.password import hash_password


@strawberry.type
class Mutation:

    @strawberry.mutation
    def register_user(
        self,
        info: Info,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> UserType:

        db = info.context.db

        existing_user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if existing_user:
            raise Exception("Email already exists")

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hash_password(password),
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return UserType(
            id=new_user.id,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            email=new_user.email,
        )

    @strawberry.mutation
    def login(
        self,
        info: Info,
        email: str,
        password: str,
    ) -> AuthResponse:

        db = info.context.db

        token, user = AuthService.login(
            db=db,
            email=email,
            password=password,
        )

        return AuthResponse(
            access_token=token,
            token_type="Bearer",
            user=UserType(
                id=user.id,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
            ),
        )