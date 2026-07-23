import swisseph as swe

print("JD UTC midnight")
print(swe.julday(2026, 6, 29, 0.0))

print()

print("JD IST midnight")
print(swe.julday(2026, 6, 28, 18.5))