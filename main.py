""""Such." declarative JSON-derived language interpreter for Python."""
from src.such_interpreter import Such

def main():
    """
    ? First, let's define how we want our language to look in the "foo.such" file.
    * Extension: .such
    * This language will have headers, which will not have an equals. May these be the keys, of which their level is defined by the double colons:

    * 1. To do something like this, we will need to at least parse a file line by line, so, let's start with that. Reading from a file. Then we'll get with the parsing.
    * 2. Now we have read information from the file, let's divide it into statements
    * 3. Once divided into statements, let's start parsing the statements and associating them.
    * 4. After parsing
    """

    fullFilePath: str = "./data/such/foo.such"
    semiFilePath: str = "./data/such/baz.such"
    reducedFilePath: str = "./data/such/bar.such"

    print(f"Reading from {reducedFilePath}...:")
    print(f"\n=============================\n```such\n{Such.from_file(reducedFilePath)}\n```")

    print(f"Reading from {semiFilePath}...:")
    print(f"\n=============================\n```such\n{Such.from_file(semiFilePath)}\n```")

    # ! Comments and headers, which are present in this file, have not been given support yet. Expect errors.
    print(f"Reading from {fullFilePath}...:")
    print(f"\n=============================\n```such\n{Such.from_file(fullFilePath)}\n```\n\n")

def large_json():
    import json
    import random
    from faker import Faker

    # Initialize Faker
    fake = Faker()

    # Generate a large JSON file with fictional data
    data = []

    # Create 100,000 fictional records
    for i in range(50000):
        record = {f"employee{i}": {
            "id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address(),
            "phone_number": fake.phone_number(),
            "job": fake.job(),
            "company": fake.company(),
            "birthdate": fake.date_of_birth().isoformat(),
            "created_at": fake.date_time_this_decade().isoformat(),
            "is_active": random.choice([True, False]),
            "age": random.randint(18,65),
            "car": None
        }}
        data.append(record)

    # Save to a JSON file
    with open("tests/examples/write_examples/json/full_final.json", "w") as f:
        json.dump(data, f)


if __name__ == '__main__':
    large_json()
