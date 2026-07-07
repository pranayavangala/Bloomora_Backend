from app.utils.jwt import verify_token


def get_current_email(info):

    request = info.context.request

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return None

    if not auth_header.startswith("Bearer "):
        return None

    token = auth_header.replace("Bearer ", "")

    payload = verify_token(token)

    if payload is None:
        return None

    return payload.get("sub")