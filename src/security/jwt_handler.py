from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "recruitverse_secret"
ALGORITHM = "HS256"


def create_token(username):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])