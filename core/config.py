from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    # db_echo: bool = False
    db_echo: bool = True
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    ALGORITHM: str = "RS256"

    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    token_expire_minutes: int = 3

    def get_db_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"


settings = Settings()
