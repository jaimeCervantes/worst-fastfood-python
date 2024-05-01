from passlib.context import CryptContext


password_ctx =  CryptContext(schemes=["bcrypt"], deprecated="auto")
def generate_hashedPassword(password: str):
    return password_ctx.hash(password)

def verify_password(password: str, hashed_password: str):
    return password_ctx.verify(password, hashed_password)
