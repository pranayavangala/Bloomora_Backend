from strawberry.fastapi import BaseContext
from fastapi import Request
from sqlalchemy.orm import Session


class GraphQLContext(BaseContext):

    def __init__(self, db: Session, request: Request):
        self.db = db
        self.request = request