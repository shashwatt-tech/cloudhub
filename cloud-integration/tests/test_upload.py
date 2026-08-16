import pytest
from appetize_client import AppetizeClient


@pytest.fixture
def client():
    """Create a client instance for testing"""
    return AppetizeClient()


def test_client_initialization(client):
    """Test that client initializes correctly"""
    assert client is not None
    assert client.api_url is not None
    assert client.api_token is not None
    print("✅ Client initialization test passed!")


def test_connection(client):
    """Test API connection"""
    result = client.test_connection()
    assert result is True
    print("✅ Connection test passed!")


def test_list_apps(client):
    """Test listing apps"""
    apps = client.list_apps()
    assert isinstance(apps, list)
    print(f"✅ List apps test passed! Found {len(apps)} apps")


def test_upload_nonexistent_file(client):
    """Test upload with non-existent file"""
    with pytest.raises(FileNotFoundError):
        client.upload_apk("nonexistent_file.apk")

    print("✅ File not found test passed!")