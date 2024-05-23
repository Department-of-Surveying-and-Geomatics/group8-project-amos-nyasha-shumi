import csv
import math


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


def calculate_distance(point1, point2):
    x1, y1 = point1[1], point1[2]
    x2, y2 = point2[1], point2[2]

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def calculate_bearing(point1, point2):
    x1, y1 = point1[1], point1[2]
    x2, y2 = point2[1], point2[2]

    dx = x2 - x1
    dy = y2 - y1

    bearing = math.atan2(dy, dx)
    bearing_degrees = math.degrees(bearing)

    return bearing_degrees


# Example usage:
file_path = 'traverse_data.csv'
traverse_data = read_traverse_data(file_path)

# Calculate traverse characteristics
total_points = len(traverse_data)
easting_values = [point[1] for point in traverse_data]
northing_values = [point[2] for point in traverse_data]
min_easting = min(easting_values)
max_easting = max(easting_values)
min_northing = min(northing_values)
max_northing = max(northing_values)

print(f"Total Points: {total_points}")
print(f"Minimum Easting: {min_easting}")
print(f"Maximum Easting: {max_easting}")
print(f"Minimum Northing: {min_northing}")
print(f"Maximum Northing: {max_northing}")

# Calculate distance and bearing between two points provided by the user
point1_index = int(input("Enter the index of the first point: "))
point2_index = int(input("Enter the index of the second point: "))

if point1_index < 0 or point1_index >= total_points or point2_index < 0 or point2_index >= total_points:
    print("Error: Invalid point index.")
else:
    point1 = traverse_data[point1_index]
    point2 = traverse_data[point2_index]

    distance = calculate_distance(point1, point2)
    bearing = calculate_bearing(point1, point2)

    print(f"Distance between point {point1_index} and point {point2_index}: {distance}")
    print(f"Bearing between point {point1_index} and point {point2_index}: {bearing} degrees")