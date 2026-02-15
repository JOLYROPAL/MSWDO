from io import BytesIO

from fastapi.testclient import TestClient
from PIL import Image

from app.main import app
from security.branding_policy import BrandingPolicy


client = TestClient(app)


def test_theme_endpoint_returns_official_palette():
    response = client.get('/api/v1/branding/theme')
    assert response.status_code == 200
    payload = response.json()
    assert payload['primary_blue'] == '#2e3192'
    assert payload['primary_red'] == '#ee1c25'
    assert payload['primary_yellow'] == '#fef200'
    assert payload['font_family'] == 'Arial'


def test_logo_policy_rejects_non_square_ratio():
    image = Image.new('RGB', (200, 100), color='white')
    buffer = BytesIO()
    image.save(buffer, format='PNG')

    try:
        BrandingPolicy().validate_logo('image/png', buffer.getvalue())
    except ValueError as exc:
        assert 'aspect ratio' in str(exc)
        return

    raise AssertionError('Expected aspect ratio validation to fail.')
