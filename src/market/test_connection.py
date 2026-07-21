"""
Sprint 20A - Kite Authentication Test

Purpose:
--------
1. Authenticate with Zerodha Kite.
2. Generate an access token.
3. Verify API connectivity.
4. Print the logged-in user profile.

Author: NakshatraAlpha
"""

import os

from dotenv import load_dotenv
from kiteconnect import KiteConnect

# --------------------------------------------------
# Load API credentials from .env
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("KITE_API_KEY")
API_SECRET = os.getenv("KITE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise ValueError(
        "KITE_API_KEY or KITE_API_SECRET not found. "
        "Please check your .env file."
    )

# --------------------------------------------------
# Initialize Kite Connect
# --------------------------------------------------

kite = KiteConnect(api_key=API_KEY)

print("\nOpen this URL in your browser:\n")
print(kite.login_url())

print("\nAfter login, Zerodha will redirect you.")
print("Copy ONLY the request_token from the redirected URL.\n")

request_token = input("Paste request_token here: ").strip()

try:
    # Generate session
    session = kite.generate_session(
        request_token=request_token,
        api_secret=API_SECRET
    )

    access_token = session["access_token"]

    # Set access token
    kite.set_access_token(access_token)

    print("\n✅ Login Successful")
    print("=" * 70)

    # Fetch user profile
    profile = kite.profile()

    print(profile)

    print("=" * 70)
    print("\nAccess Token:\n")
    print(access_token)

except Exception as e:
    print("\n❌ Authentication Failed")
    print(f"Reason: {e}")