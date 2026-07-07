import strawberry
from strawberry.types import Info

from app.graphql.auth import get_current_email
from app.graphql.types import UserType
from app.models.user import User


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "🌸 Welcome to Bloomora GraphQL"

    @strawberry.field
    def me(self, info: Info) -> UserType | None:

        email = get_current_email(info)

        if email is None:
            return None

        db = info.context.db

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if user is None:
            return None

        return UserType(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )