"""
Kite Service

Purpose
-------
Provides a single authenticated KiteConnect client for the application.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from kiteconnect import KiteConnect

# Load .env from project root
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"

print(f"\nLoading .env from:\n{ENV_PATH}")

load_dotenv(dotenv_path=ENV_PATH, override=True)


class KiteService:
    """
    Handles Kite authentication and provides an authenticated client.
    """

    def __init__(self):

        self.api_key = os.getenv("KITE_API_KEY")
        self.access_token = os.getenv("KITE_ACCESS_TOKEN")

        print("\nAPI Key Loaded :", self.api_key)

        if self.access_token:
            print("Access Token :", self.access_token[:8] + "...")
            print("Access Token Length :", len(self.access_token))
        else:
            print("Access Token : None")

        if not self.api_key:
            raise ValueError("KITE_API_KEY missing")

        if not self.access_token:
            raise ValueError("KITE_ACCESS_TOKEN missing")

        self._kite = KiteConnect(api_key=self.api_key)
        self._kite.set_access_token(self.access_token)

    def get_client(self) -> KiteConnect:
        """
        Return the authenticated KiteConnect client.
        """
        return self._kite

    def is_connected(self) -> bool:
        """
        Verify authentication by fetching the user profile.
        """
        try:
            profile = self._kite.profile()

            print("\nAuthenticated User:")
            print(profile["user_name"])

            return True

        except Exception as e:

            print("\nAuthentication Error:")
            print(e)

            return False