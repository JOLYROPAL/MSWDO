from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_chatbot_response():
    response = client.post('/api/v1/chatbot/ask', json={'message': 'What is AICS?'})
    assert response.status_code == 200
    assert 'AICS' in response.json()['answer']
