import csv
import random
from faker import Faker

# Initialize a Faker generator
fake = Faker()

# Define the number of rows of data to create
num_rows = 100000

# Define the filename for the output CSV file
filename = 'data.csv'

# Function to generate an email based on name and surname, with a random number to ensure uniqueness
def generate_email(name, surname, existing_emails):
    # Try to generate a unique email address
    for _ in range(10):  # Retry 10 times if necessary
        number = random.randint(1, 99999)
        email = f"{name.lower()}.{surname.lower()}{number}@example.com"
        if email not in existing_emails:
            return email
    raise ValueError(f"Could not generate a unique email for {name} {surname}")

# Set to keep track of existing emails
existing_emails = set()

# Open a CSV file for writing
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['name', 'surname', 'email'])

    # Generate and write the data rows
    for _ in range(num_rows):
        name = fake.first_name()
        surname = fake.last_name()
        email = generate_email(name, surname, existing_emails)
        writer.writerow([name, surname, email])
        existing_emails.add(email)

print(f"Created {num_rows} rows in the file '{filename}'")