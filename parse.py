data = [
    {"name": "Lokesh", "age": "24", "city": "New York"},
    {"name": "Sesham", "age": "22", "city": "Los Angeles"},
    {"name": "Ram", "age": "44", "city": "Chicago"}
]

spec = [10, 3, 15]

def generate_fixed_width_file(data, spec, filename):
    with open(filename, 'w') as f:
        for row in data:
            line = ''
            for i, key in enumerate(row):
                value = str(row[key])
                line += value.ljust(spec[i])
            f.write(line + '\n')

generate_fixed_width_file(data, spec, 'fixed_width_file.txt')

# Parse fixed width file to CSV
import csv

def parse_fixed_width_file(input_file, output_file, spec):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for line in infile:
            row = []
            start = 0
            for width in spec:
                field = line[start:start + width].strip()
                row.append(field)
                start += width
            writer.writerow(row)

parse_fixed_width_file('fixed_width_file.txt', 'output.csv', spec)
