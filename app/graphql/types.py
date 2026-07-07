import strawberry


@strawberry.type
class UserType:

    id: int

    first_name: str

    last_name: str

    email: str


@strawberry.type
class AuthResponse:

    access_token: str

    token_type: str

    user: UserType

@strawberry.type
class AIResponse:
    response: str
@strawberry.type
class ChatType:
        id: int

        role: str

        message: str