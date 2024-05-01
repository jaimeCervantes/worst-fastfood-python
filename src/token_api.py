from dotenv import load_dotenv
import os
import jwt
from datetime import datetime, timedelta, timezone

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRES_ON_MINUTES = os.getenv("EXPIRES_ON_MINUTES")

if not SECRET_KEY:
    raise ValueError("No secret key provided. Make sure to set SECRET_KEY in your .env file.")


def generate_jwt_token(payload):
    # El token sera valido por una hora
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=float(EXPIRES_ON_MINUTES))
    payload['exp'] = expiration_time
    return jwt.encode(payload, SECRET_KEY, algorithm=str(ALGORITHM))

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[str(ALGORITHM)])
        return payload
    except jwt.ExpiredSignatureError:
        # Ya expiró el token
        return None
    except jwt.InvalidTokenError:
        # Invalido
        return None
