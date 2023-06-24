import random

from datetime import datetime, timedelta
    

# 2023-06-23T20:14:17+07:00

def generate_random_date(start_date, end_date):
    # Calculate the time range in seconds
    time_range = (end_date - start_date).total_seconds()

    # Generate a random number of seconds to add to the start date
    random_seconds = random.randint(0, int(time_range))

    # Calculate the random date
    random_date = start_date + timedelta(seconds=random_seconds)

    # Format the random date with timezone offset
    formatted_date = random_date.strftime("%Y-%m-%dT%H:%M:%S%z")

    return formatted_date


# Example usage
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 6, 24)

random_date = generate_random_date(start_date, end_date)

print(random_date)

dt = datetime.fromisoformat(random_date)
formatted_date = dt.strftime("%Y-%m-%d")
print(formatted_date)

import re

ttl = "h^&ell`.,|o w]{+orld"
ttl2 = "﻿HEELow`* |W ❤ Wo()rLD"
ttl3 = "FAYOLA Daily hijab simpel renda manis Quail Hijab bahan wolly crepe"

def get_title(title):
    if re.match('^[^a-zA-Z]', title, re.I):
        s = re.sub('^[^a-zA-Z]', 'aaaaa-', title)
    else:
        s = title
    return s

def get_brand(title):
    if re.match(r'^(?=.*\bquail?\b).*$', title, re.I):
        brand = "Quail"
    elif re.match(r'^(?=.*\byessana?\b).*$', title, re.I):
        brand = "Yessana"
    else:
        brand = "Mewlena"
    
    return brand

s = re.sub('^[^a-zA-Z]', 'aaaaa-', ttl2)
print(get_brand(ttl3))

