import swisseph as swe

print("PySwissEph Version :", swe.version)

print("\nRise related functions:")
for name in dir(swe):
    if "rise" in name.lower():
        print(name)

print("\nRelevant constants:")
for name in dir(swe):
    if "CALC_RISE" in name or "SET" in name or "HINDU" in name:
        print(name)