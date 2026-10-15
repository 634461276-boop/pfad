from fastapi.testclient import TestClient
from week04.api import app

client = TestClient(app)

def test_september_tides_returns_daily_records():
    response = client.get("/tides?month=9")
    assert response.status_code == 200
    rows = response.json()
    assert rows[0]["month"] == 9
    assert rows[0]["day"] == 1
    assert len(rows[0]["heights"]) == 24
    assert all(isinstance(height, (int, float)) for height in rows[0]["heights"])