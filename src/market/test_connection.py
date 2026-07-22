"""
Sprint 20A - Kite Authentication

Purpose
-------
1. Authenticate with Zerodha.
2. Generate a new access token.
3. Automatically update .env.
4. Verify authentication.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from kiteconnect import KiteConnect

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_FILE, override=True)

API_KEY = os.getenv("KITE_API_KEY")
API_SECRET = os.getenv("KITE_API_SECRET")

if not API_KEY:
    raise ValueError("KITE_API_KEY not found.")

if not API_SECRET:
    raise ValueError("KITE_API_SECRET not found.")

kite = KiteConnect(api_key=API_KEY)

print("\nOpen this URL in your browser:\n")
print(kite.login_url())

print("\nAfter login, copy ONLY the request_token.\n")

request_token = input("Request Token : ").strip()

try:

    session = kite.generate_session(
        request_token=request_token,
        api_secret=API_SECRET,
    )

    access_token = session["access_token"]

    kite.set_access_token(access_token)

    profile = kite.profile()

    print("\n" + "=" * 70)
    print("LOGIN SUCCESSFUL")
    print("=" * 70)

    print(f"User      : {profile['user_name']}")
    print(f"User ID   : {profile['user_id']}")

    # ---------------------------------------------
    # Update .env automatically
    # ---------------------------------------------

    lines = ENV_FILE.read_text(
        encoding="utf-8"
    ).splitlines()

    updated = False

    for i, line in enumerate(lines):

        if line.startswith("KITE_ACCESS_TOKEN="):
            lines[i] = f"KITE_ACCESS_TOKEN={access_token}"
            updated = True

    if not updated:
        lines.append(f"KITE_ACCESS_TOKEN={access_token}")

    ENV_FILE.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print("\n✅ .env updated successfully.")

    # ---------------------------------------------
    # Verify by creating a NEW client
    # ---------------------------------------------

    verifier = KiteConnect(api_key=API_KEY)
    verifier.set_access_token(access_token)

    verifier.profile()

    print("✅ Token verification successful.")
    print("\nNo manual copy/paste required anymore.")

except Exception as e:

    print("\nAuthentication Failed")
    print(e)    