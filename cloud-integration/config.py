import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APPETIZE_API_TOKEN = os.getenv("APPETIZE_API_TOKEN")

    APPETIZE_API_URL = os.getenv(
        "APPETIZE_API_URL",
        "https://api.appetize.io/v1"
    )

    @classmethod
    def validate(cls):
        if not cls.APPETIZE_API_TOKEN:
            raise ValueError(
                "❌ APPETIZE_API_TOKEN not found in .env file!"
            )

        print("✅ Configuration validated successfully!")
        return True


if __name__ == "__main__":
    try:
        Config.validate()
        print(f"📡 API URL: {Config.APPETIZE_API_URL}")
        print(f"🔑 Token: {Config.APPETIZE_API_TOKEN[:10]}...")
    except ValueError as e:
        print(e)