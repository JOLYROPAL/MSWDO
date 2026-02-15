from security.branding_policy import BrandingPolicy


class ThemeService:
    def __init__(self, policy: BrandingPolicy):
        self.policy = policy

    def get_locked_theme(self) -> dict[str, str]:
        theme = self.policy.allowed_theme()
        return {
            "primary_blue": theme.primary_blue,
            "primary_red": theme.primary_red,
            "primary_yellow": theme.primary_yellow,
            "neutral_dark_blue": theme.neutral_dark_blue,
            "neutral_gray_light": theme.neutral_gray_light,
            "neutral_gray_dark": theme.neutral_gray_dark,
            "neutral_khaki": theme.neutral_khaki,
            "font_family": theme.font_family,
        }
