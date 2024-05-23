import csv
import matplotlib.pyplot as plt

def plot_traverse(file_path):
    points = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            x = float(row['Easting'])
            y = float(row['Northing'])
            points.append((x, y))

    # Extract x and y coordinates
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    point_numbers = list(range(1, len(points) + 1))  # Generate point numbers

    # Create scatter plot
    plt.figure(figsize=(8, 6))  # Adjust the figure size
    plt.scatter(x_coords, y_coords, c='blue', alpha=0.7)

    # Add point numbers as annotations
    for i, point in enumerate(points):
        plt.annotate(str(point_numbers[i]), (point[0], point[1]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

    # Set plot title and labels
    plt.title("Traverse Scatter Plot")
    plt.xlabel("Easting")
    plt.ylabel("Northing")
    plt.grid(True)  # Add grid lines

    # Add legend
    plt.legend(['Traverse Points'], loc='upper left')

    # Display the plot
    plt.show()

# Example usage
traverse_file = 'traverse_data.csv'
plot_traverse(traverse_file)