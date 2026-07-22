from src.market.kite_service import KiteService
from src.market.instrument_repository import InstrumentRepository

service = KiteService()

if not service.is_connected():
    raise RuntimeError("Kite is not connected.")

kite = service.get_client()

repo = InstrumentRepository(kite)

print(repo.get("NIFTY"))
print(repo.get("BANKNIFTY"))
print(repo.get("RELIANCE"))

print()

print(repo.get("NIFTY").is_index)
print(repo.get("RELIANCE").is_equity)

print()

print(repo.token("NIFTY"))