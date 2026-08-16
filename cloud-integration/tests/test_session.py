import pytest
from appetize_client import AppetizeClient
import time


@pytest.fixture
def client():
    """Create a client instance for testing"""
    return AppetizeClient()


@pytest.fixture
def app_public_key(client):
    """Get a public key for testing"""

    apps = client.list_apps()

    if apps:
        return apps[0]["publicKey"]

    pytest.skip("No apps available for testing")


def test_create_session(client, app_public_key):
    """Test session creation"""

    session = client.create_session(app_public_key)

    assert "sessionId" in session
    assert session["sessionId"] is not None

    # Clean up
    client.stop_session(session["sessionId"])

    print("✅ Create session test passed!")


def test_get_session_info(client, app_public_key):
    """Test getting session info"""

    session = client.create_session(app_public_key)
    session_id = session["sessionId"]

    info = client.get_session_info(session_id)

    assert info is not None

    # Clean up
    client.stop_session(session_id)

    print("✅ Get session info test passed!")


def test_stop_session(client, app_public_key):
    """Test stopping a session"""

    session = client.create_session(app_public_key)
    session_id = session["sessionId"]

    time.sleep(2)

    result = client.stop_session(session_id)

    assert result["status"] == "stopped"
    assert result["sessionId"] == session_id

    print("✅ Stop session test passed!")


def test_invalid_session_id(client):
    """Test with invalid session ID"""

    with pytest.raises(Exception):
        client.stop_session("invalid_session_id_123456")

    print("✅ Invalid session ID test passed!")