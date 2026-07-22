from astrology.navamsha import navamsha_details

print("=" * 50)

for longitude in [0, 15, 29.99, 45, 120, 215.5, 359.99]:
    print(f"Longitude: {longitude}")
    print(navamsha_details(longitude))
    print("-" * 50)