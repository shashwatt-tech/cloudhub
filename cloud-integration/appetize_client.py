import requests
from config import Config


class AppetizeClient:
    """Client for interacting with Appetize.io API."""

    def __init__(self):
        self.api_url = Config.APPETIZE_API_URL
        self.api_token = Config.APPETIZE_API_TOKEN

        self.headers = {
            "X-API-KEY": self.api_token
        }

        print("🚀 AppetizeClient initialized!")

    def test_connection(self):
        try:
            response = requests.get(
                f"{self.api_url}/apps",
                headers=self.headers,
                timeout=30
            )

            response.raise_for_status()

            print("✅ Connection successful!")

            try:
                data = response.json()
                print("📱 Apps:")
                print(data)
            except ValueError:
                print("Response:", response.text)

            return True

        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP Error: {e}")
            print(f"📄 Response: {response.text}")
            return False

        except requests.exceptions.RequestException as e:
            print(f"❌ Connection failed: {e}")
            return False

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False


if __name__ == "__main__":
    client = AppetizeClient()
    client.test_connection()