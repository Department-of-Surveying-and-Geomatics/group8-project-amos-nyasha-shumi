import csv


def read_traverse_data(file_path):
    traverse_data = []

    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)

            # Skip the header row if present
            next(csv_reader)

            for row in csv_reader:
                try:
                    point_number = int(row[0])
                    easting = float(row[1])
                    northing = float(row[2])

                    traverse_data.append((point_number, easting, northing))
                except (ValueError, IndexError):
                    print(f"Error: Invalid data format in row {csv_reader.line_num}. Skipping row.")
    except FileNotFoundError:
        print("Error: File not found.")

    return traverse_data


# Example usage:
file_path = 'traverse_data.csv'
traverse_data = read_traverse_data(file_path)

# Print the traverse data
for point in traverse_data:
    point_number, easting, northing = point
    print(f"Point {point_number}: Easting={easting}, Northing={northing}")