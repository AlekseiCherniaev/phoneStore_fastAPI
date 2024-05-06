import re
from datetime import timedelta, datetime

import jwt
import bcrypt
from core.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.private_key_path.read_text(),
    algorithm: str = settings.ALGORITHM,
    expire_minutes: int = settings.token_expire_minutes,
    expire_time_delta: timedelta | None = None,
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_time_delta:
        expire = now + expire_time_delta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(exp=expire, iat=now)
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.public_key_path.read_text(),
    algorithm: str = settings.ALGORITHM,
):
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
    )
    return decoded


def hash_password(
    password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
    password: str,
    hashed_password: bytes,
) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password=hashed_password)


def password_check_complexity(password: str) -> bool:
    password_regex = (
        r"^([a-zA-Z0-9$@$!%*#?&.]*$)"
    )
    pattern = re.compile(password_regex)
    return bool(pattern.match(password))
