import csv
import random
import string

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_csv(filename, num_records):
    with open(filename, 'wb') as csvfile:  # Change 'w' to 'wb' for binary mode
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow({
                'first_name': random_string(8),
                'last_name': random_string(10),
                'address': random_string(15),
                'date_of_birth': '{}-{:02d}-{:02d}'.format(random.randint(1950, 2000),
                                                          random.randint(1, 12),
                                                          random.randint(1, 28))
            })

generate_csv('data.csv', 2000000)  # Adjust the number of records as needed