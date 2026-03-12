import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")

    assert res.status_code == 200
    assert res.json["status"] == "ok"