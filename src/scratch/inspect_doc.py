import swisseph as swe
import inspect

print("=" * 80)
print("Signature")
print("=" * 80)

try:
    print(inspect.signature(swe.rise_trans))
except Exception as e:
    print(e)

print()

print("=" * 80)
print("Help")
print("=" * 80)

help(swe.rise_trans)

print()

print("=" * 80)
print("__doc__")
print("=" * 80)

print(swe.rise_trans.__doc__)