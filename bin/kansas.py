import json
import random
import sys

srcdata = [
    {
        "state": "KS",
        "data": [
            {
                "city": "Kansas City",
                "phone": "(913) 233",
                "address": ["Wood Ave", "Clay Edwards Dr"],
                "zipcode": ["66112"]
            },
            {
                "city": "Columbus",
                "phone": "(620) 674",
                "address": ["SW 20th St"],
                "zipcode": ["66725"]
            },
            {
                "city": "Mound City",
                "phone": "(913) 756",
                "address": ["Sumac Dr"],
                "zipcode": ["66056"]
            },
            {
                "city": "Salina",
                "phone": "(785) 820",
                "address": ["Eastridge Dr"],
                "zipcode": ["67401"]
            },
            {
                "city": "Sterling",
                "phone": "(620) 204",
                "address": ["E Monroe St"],
                "zipcode": ["67579"]
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
        full_address = f"{street_number} {street_name}, {city}, Kansas {zipcode}"
        phone_suffix = ''.join(random.choices('0123456789', k=4))
        phone_number = f"{phone_prefix}-{phone_suffix}"

        if (full_address, phone_number) not in existing_addresses:
            existing_addresses.add((full_address, phone_number))
            return {
                "address": full_address,
                "city": city,
                "state": "KS",
                "state2": "Kansas",
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
    database[0]["data"]["KS"].append(random_address)

with open("database.json", "w") as file:
    json.dump(database, file, indent=2)

print(f"{num_addresses} Address has been saved in database.json.")