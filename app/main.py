from fastapi import FastAPI, Request
from strawberry.fastapi import GraphQLRouter

from app.database.database import Base, SessionLocal, engine
from app.models.user import User
from app.graphql.context import GraphQLContext
from app.graphql.schema import schema

from app.models.chat import Chat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bloomora GraphQL API")


async def get_context(request: Request):

    db = SessionLocal()

    return GraphQLContext(
        db=db,
        request=request
    )

graphql_app = GraphQLRouter(
    schema=schema,
    context_getter=get_context,
)

app.include_router(
    graphql_app,
    prefix="/graphql",
)


@app.get("/")
def home():
    return {
        "message": "Bloomora API Running"
    }