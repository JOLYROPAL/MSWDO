from dataclasses import dataclass
from io import BytesIO

from PIL import Image

from app.core.config import settings


@dataclass(frozen=True)
class BrandingTheme:
    primary_blue: str
    primary_red: str
    primary_yellow: str
    neutral_dark_blue: str
    neutral_gray_light: str
    neutral_gray_dark: str
    neutral_khaki: str
    font_family: str


class BrandingPolicy:
    def allowed_theme(self) -> BrandingTheme:
        return BrandingTheme(
            primary_blue=settings.dswd_primary_blue,
            primary_red=settings.dswd_primary_red,
            primary_yellow=settings.dswd_primary_yellow,
            neutral_dark_blue=settings.dswd_neutral_dark_blue,
            neutral_gray_light=settings.dswd_neutral_gray_light,
            neutral_gray_dark=settings.dswd_neutral_gray_dark,
            neutral_khaki=settings.dswd_neutral_khaki,
            font_family=settings.dswd_font_family,
        )

    def validate_logo(self, content_type: str, raw_bytes: bytes) -> None:
        if content_type not in settings.allowed_logo_types:
            raise ValueError("Invalid logo format. Only PNG and JPEG are allowed.")
        if len(raw_bytes) > settings.max_logo_size_bytes:
            raise ValueError("Logo file exceeds maximum allowed size.")

        with Image.open(BytesIO(raw_bytes)) as img:
            width, height = img.size
            if height == 0:
                raise ValueError("Invalid image dimensions.")
            ratio = width / height
            expected = settings.logo_aspect_ratio
            tolerance = settings.logo_aspect_ratio_tolerance
            if ratio < (expected - tolerance) or ratio > (expected + tolerance):
                raise ValueError("Logo aspect ratio is not compliant with DSWD branding standards.")
