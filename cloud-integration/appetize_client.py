import requests
from typing import Dict, Any
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

    # =========================================================
    # STEP 14: TEST CONNECTION
    # =========================================================

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

    # =========================================================
    # STEP 15: UPLOAD APK
    # =========================================================

    def upload_apk(
        self,
        apk_path: str,
        app_name: str = None
    ) -> Dict[str, Any]:
        """
        Upload an APK file to Appetize.io.
        """

        print(f"📤 Starting upload: {apk_path}")

        try:
            import os

            if not os.path.exists(apk_path):
                raise FileNotFoundError(
                    f"APK file not found: {apk_path}"
                )

            with open(apk_path, "rb") as apk_file:

                files = {
                    "file": (
                        os.path.basename(apk_path),
                        apk_file,
                        "application/vnd.android.package-archive"
                    )
                }

                data = {}

                if app_name:
                    data["note"] = app_name

                upload_url = f"{self.api_url}/apps"

                print(f"🌐 Uploading to: {upload_url}")

                response = requests.post(
                    upload_url,
                    headers=self.headers,
                    files=files,
                    data=data,
                    timeout=120
                )

                response.raise_for_status()

                result = response.json()

                print("✅ APK uploaded successfully!")

                print(
                    f"📱 Public Key: "
                    f"{result.get('publicKey')}"
                )

                print(
                    f"🔗 App URL: "
                    f"{result.get('publicURL')}"
                )

                return result

        except FileNotFoundError as e:
            print(f"❌ {e}")
            raise

        except requests.exceptions.RequestException as e:
            print(f"❌ Upload failed: {e}")
            raise

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            raise

    # =========================================================
    # STEP 16: LIST APPS
    # =========================================================

    def list_apps(self) -> list:
        """
        List all apps in your Appetize account.
        """

        print("📋 Fetching apps list...")

        try:
            apps_url = f"{self.api_url}/apps"

            response = requests.get(
                apps_url,
                headers=self.headers,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            print("🔍 API Response:")
            print(data)

            # If API directly returns a list
            if isinstance(data, list):
                apps = data

            # If API returns a dictionary
            elif isinstance(data, dict):

                # Common response format
                if isinstance(data.get("apps"), list):
                    apps = data["apps"]

                # Another possible format
                elif isinstance(data.get("data"), list):
                    apps = data["data"]

                # Another possible format
                elif isinstance(data.get("items"), list):
                    apps = data["items"]

                else:
                    apps = []

            else:
                apps = []

            print(f"✅ Found {len(apps)} app(s)")

            # Print app details
            for i, app in enumerate(apps, 1):

                if isinstance(app, dict):

                    print(
                        f"\n  {i}. "
                        f"{app.get('note', 'Unnamed App')}"
                    )

                    print(
                        f"     Key: "
                        f"{app.get('publicKey', 'N/A')}"
                    )

                    print(
                        f"     Platform: "
                        f"{app.get('platform', 'unknown')}"
                    )

                else:
                    print(
                        f"\n  {i}. {app}"
                    )

            return apps

        except requests.exceptions.RequestException as e:
            print(
                f"❌ Failed to list apps: {e}"
            )
            raise

    # =========================================================
    # STEP 18: CREATE SESSION
    # =========================================================

    def create_session(
        self,
        public_key: str,
        device: str = "pixel7"
    ) -> Dict[str, Any]:
        """
        Create a new device session.
        """

        print(
            f"🎮 Creating session for app: "
            f"{public_key}"
        )

        try:
            session_url = (
                f"{self.api_url}/apps/"
                f"{public_key}/sessions"
            )

            payload = {
                "device": device,
                "osVersion": "13.0",
                "timeout": 300
            }

            print(
                f"📱 Device: {device}, "
                f"OS: Android 13.0"
            )

            response = requests.post(
                session_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )

            response.raise_for_status()

            result = response.json()

            print(
                "✅ Session created successfully!"
            )

            print(
                f"🆔 Session ID: "
                f"{result.get('sessionId')}"
            )

            print(
                f"🌐 Session URL: "
                f"{result.get('url')}"
            )

            return result

        except requests.exceptions.RequestException as e:
            print(
                f"❌ Session creation failed: {e}"
            )
            raise

    # =========================================================
    # STEP 18: GET SESSION INFO
    # =========================================================

    def get_session_info(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """
        Get information about a session.
        """

        print(
            f"ℹ️ Getting info for session: "
            f"{session_id}"
        )

        try:
            session_url = (
                f"{self.api_url}/sessions/"
                f"{session_id}"
            )

            response = requests.get(
                session_url,
                headers=self.headers,
                timeout=30
            )

            response.raise_for_status()

            result = response.json()

            print(
                "✅ Session info retrieved"
            )

            return result

        except requests.exceptions.RequestException as e:
            print(
                f"❌ Failed to get session info: "
                f"{e}"
            )
            raise

    # =========================================================
    # STEP 18: STOP SESSION
    # =========================================================

    def stop_session(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """
        Stop an active session.
        """

        print(
            f"🛑 Stopping session: "
            f"{session_id}"
        )

        try:
            session_url = (
                f"{self.api_url}/sessions/"
                f"{session_id}"
            )

            response = requests.delete(
                session_url,
                headers=self.headers,
                timeout=30
            )

            response.raise_for_status()

            print(
                "✅ Session stopped successfully!"
            )

            return {
                "status": "stopped",
                "sessionId": session_id
            }

        except requests.exceptions.RequestException as e:
            print(
                f"❌ Failed to stop session: "
                f"{e}"
            )
            raise


# =============================================================
# TEST THE CLIENT
# =============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("🧪 Testing AppetizeClient")
    print("=" * 50)

    client = AppetizeClient()

    # Test connection
    print("\n1️⃣ Testing connection...")
    client.test_connection()

    # Test list apps
    print("\n2️⃣ Testing list apps...")
    apps = client.list_apps()

    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("=" * 50)