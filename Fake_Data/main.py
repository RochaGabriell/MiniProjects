import json
from faker import Faker

fake = Faker()

data_dictionary = []

for cont in range(0, 10):
    data_dictionary.append({
        "name" : fake.name(),
        "first_name" : fake.first_name(),
        "user" : fake.user_name(),
        "password" : fake.password(),
        "month" : fake.month()
    })

for cont in data_dictionary:
    print(json.dumps(cont, sort_keys=True, indent=4))