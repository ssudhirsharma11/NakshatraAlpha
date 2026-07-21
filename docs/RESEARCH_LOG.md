# Research Log

---

# Sprint 20 – Market Data Engine

**Status:** 🚧 In Progress

**Start Date:** 21-Jul-2026

## Objective

Build the complete Market Data Engine that will integrate historical market data into NakshatraAlpha and enable objective backtesting.

---

## Sprint 20A – Authentication Engine ✅

### Completed

- Created Zerodha Kite Connect application.
- Generated API Key.
- Generated API Secret.
- Configured Redirect URL.
- Installed Kite Connect SDK.
- Created `src/market` module.
- Created `kite_service.py`.
- Created `test_connection.py`.
- Successfully authenticated with Zerodha.
- Generated Access Token.
- Successfully fetched Zerodha profile.
- Verified API connectivity.

---

### Issues Encountered

#### Issue 1 – Invalid API Key

**Cause**

Incorrect API Key used during initial testing.

**Resolution**

Updated to the correct API Key.

---

#### Issue 2 – Invalid Checksum

**Cause**

API Secret had changed after app creation.

**Resolution**

Updated to the latest API Secret.

---

#### Issue 3 – Redirect URL Connection Refused

**Cause**

No local server was listening on `127.0.0.1:5000`.

**Resolution**

Expected behaviour for manual authentication.
Copied the `request_token` manually from the redirected URL.

---

## Outcome

✅ NakshatraAlpha can now communicate securely with Zerodha Kite APIs.

This completes the Authentication Engine.

---

## Next Milestone

### Sprint 20B – Historical Data Downloader

Deliverables:

- Download Instrument Master
- Instrument Token Manager
- Historical Candle Downloader
- CSV Storage
- Data Validation

---

## Notes

Authentication is currently manual.

Future improvement:

Automate the login flow using a local callback server so the `request_token` is captured automatically.

---

## Research Impact

This milestone establishes the Market Data Layer, which bridges the existing Astronomy Engine with real historical market data.

It is the first step toward objective validation of planetary hypotheses.