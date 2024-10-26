import json
import random
import sys

srcdata = [
    {
        "state": "NJ",
        "data": [
            {
                "city": "Jackson",
                "phone": "(732) 833",
                "address": ["Challenger Way"],
                "zipcode": ["08527"]
            },
            {
                "city": "Hackensack",
                "phone": "(201) 342",
                "address": ["James St"],
                "zipcode": ["07601"]
            },
            {
                "city": "Haddonfield",
                "phone": "(803) 648",
                "address": ["Kings Hwy E"],
                "zipcode": ["08033"]
            },
            {
                "city": "Dover",
                "phone": "(973) 442",
                "address": ["Mount Hope Ave #M10"],
                "zipcode": ["07801"]
            }
        ]
    }
]

with open("database.json", "r") as file:
    database = json.load(file)

def generate_random_address(city_data, existing_addresses):
    city = city_data["city"]
    zipcode = city_data["zipcode"][0]
    phone_prefix = city_data["phone"]

    while True:
        street_name = random.choice(city_data.get("address", ["Unknown Street"]))
        street_number = random.randint(1000, 9999)
        full_address = f"{street_number} {street_name}, {city}, New Jersey {zipcode}"
        phone_suffix = ''.join(random.choices('0123456789', k=4))
        phone_number = f"{phone_prefix}-{phone_suffix}"

        if (full_address, phone_number) not in existing_addresses:
            existing_addresses.add((full_address, phone_number))
            return {
                "address": full_address,
                "city": city,
                "state": "NJ",
                "state2": "New Jersey",
                "zipcode": zipcode,
                "phone": phone_number
            }

if len(sys.argv) > 1:
    num_addresses = int(sys.argv[1])
else:
    num_addresses = int(input("How many addresses you want to generate ? "))

generated_addresses = set()

for _ in range(num_addresses):
    random_city_data = random.choice(srcdata[0]["data"])
    random_address = generate_random_address(random_city_data, generated_addresses)

    print(f"New address : {random_address}")
    database[0]["data"]["NJ"].append(random_address)

with open("database.json", "w") as file:
    json.dump(database, file, indent=2)

print(f"{num_addresses} Address has been saved in database.json.")