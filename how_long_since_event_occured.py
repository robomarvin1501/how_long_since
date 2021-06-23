import os
os.chdir("~/how_long_since")

import sys
import datetime
import factors

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print(f"Order is as follows: python how_long_since_event_occurred.py name event date_of_thing_in_iso_format")
    sys.exit()

name = sys.argv[1]
event = sys.argv[2]
date_of_event = datetime.date.fromisoformat(sys.argv[3])

delta = datetime.date.today() - date_of_event

if datetime.date.today().month == 12 and datetime.date.today().day == 21:
    print(f"{name} was {event} {datetime.date.today().year - date_of_event.year} years ago")

with open("primes_l_1mill.txt", 'r') as f:
    primes = [int(x) for x in f.read().split(',')]

text = f"{name} was {event} {delta.days} days ago"
if delta.days in primes:
    text += " which is prime"
else:
    text += f".  The factors are {factors.factors(delta.days)} and the prime factors are ({factors.format_prime_dict(factors.prime_factors(delta.days))})"

print(text)
