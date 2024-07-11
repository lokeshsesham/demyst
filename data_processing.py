import csv
import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_csv(filename, num_records):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow({
                'first_name': random_string(8),
                'last_name': random_string(10),
                'address': random_string(15),
                'date_of_birth': f"{random.randint(1950, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            })

def anonymize_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            row['first_name'] = 'ANONYMIZED'
            row['last_name'] = 'ANONYMIZED'
            row['address'] = 'ANONYMIZED'
            writer.writerow(row)

# Generate a sample CSV file
generate_csv('sample.csv', 1000)

# Anonymize the sample CSV file
anonymize_csv('sample.csv', 'anonymized_sample.csv')
