from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MSWDO Laguna Digital Services"
    environment: str = "development"
    secret_key: str = "change-me"
    access_token_expire_minutes: int = 60
    algorithm: str = "HS256"
    database_url: str = "sqlite:///./mswdo.db"
    mysql_user: str = "root"
    mysql_password: str = "root"
    mysql_host: str = "localhost"
    mysql_port: int = 3306
    mysql_db: str = "mswdo"
    cors_origins: list[str] = ["*"]

    dswd_primary_blue: str = "#2e3192"
    dswd_primary_red: str = "#ee1c25"
    dswd_primary_yellow: str = "#fef200"
    dswd_neutral_dark_blue: str = "#1f2a44"
    dswd_neutral_gray_light: str = "#f3f4f6"
    dswd_neutral_gray_dark: str = "#374151"
    dswd_neutral_khaki: str = "#c3b091"
    dswd_font_family: str = "Arial"

    max_logo_size_bytes: int = 2 * 1024 * 1024
    allowed_logo_types: tuple[str, ...] = ("image/png", "image/jpeg")
    logo_aspect_ratio: float = 1.0
    logo_aspect_ratio_tolerance: float = 0.05

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
