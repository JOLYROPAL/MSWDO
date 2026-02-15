from pydantic import BaseModel


class ThemeRead(BaseModel):
    primary_blue: str
    primary_red: str
    primary_yellow: str
    neutral_dark_blue: str
    neutral_gray_light: str
    neutral_gray_dark: str
    neutral_khaki: str
    font_family: str


class LogoUploadRead(BaseModel):
    branch_id: int
    logo_url: str
