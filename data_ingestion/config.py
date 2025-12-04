from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # =========================================================================
    # U.S. Bureau of Economic Analysis (BEA)
    # =========================================================================
    # BEA API endpoint
    BASE_URL: str = "https://apps.bea.gov/api/data/"

    BEA_API_KEY: str = "YOUR_API_KEY_HERE"

    # =========================================================================
    # PostgreSQL
    # =========================================================================
    DB_USER: str = "superset"
    DB_PASS: str = "superset"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "superset"

    @property
    def db_dsn(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
