"""
Sprint 20B - Kite Service

Purpose:
- Read API credentials from .env
- Create an authenticated KiteConnect client
- Verify the connection
"""

import os

from dotenv import load_dotenv
from kiteconnect import KiteConnect

load_dotenv()


class KiteService:
    """Service responsible for Zerodha Kite authentication."""

    def __init__(self):
        self.api_key = os.getenv("KITE_API_KEY")
        self.access_token = os.getenv("KITE_ACCESS_TOKEN")

        if not self.api_key:
            raise ValueError("KITE_API_KEY not found in .env")

        if not self.access_token:
            raise ValueError("KITE_ACCESS_TOKEN not found in .env")

        self.kite = KiteConnect(api_key=self.api_key)
        self.kite.set_access_token(self.access_token)

    def connect(self):
        """
        Returns an authenticated KiteConnect client.
        """
        return self.kite

    def is_connected(self) -> bool:
        """
        Returns True if the access token is valid.
        """
        try:
            self.kite.profile()
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def logout(self):
        """
        Clears the local Kite client.
        """
        self.kite = None