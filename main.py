import csv
import math
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def calculate_distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points using the Pythagorean theorem.
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_bearing(x1, y1, x2, y2):
    """
    Calculates the bearing between two points using the arctangent function.
    """
    dx = x2 - x1
    dy = y2 - y1
    return math.degrees(math.atan2(dy, dx))

def calculate_traverse_characteristics(file_path, point1, point2):
    points = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            x = float(row['Easting'])
            y = float(row['Northing'])
            points.append((x, y))

    distance = calculate_distance(points[point1][0], points[point1][1], points[point2][0], points[point2][1])
    bearing = calculate_bearing(points[point1][0], points[point1][1], points[point2][0], points[point2][1])

    return distance, bearing

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

    # Create scatter plot
    plt.figure(figsize=(10, 8))
    plt.scatter(x_coords, y_coords)

    # Add point numbers as annotations
    for i, point in enumerate(points):
        plt.annotate(str(i), (point[0], point[1]), textcoords="offset points", xytext=(0,10), ha='center')

    # Connect the points with lines
    for i in range(len(points) - 1):
        plt.plot([points[i][0], points[i+1][0]], [points[i][1], points[i+1][1]], '-', color='r')

    # Set plot title and labels
    plt.title("Traverse Plot")
    plt.xlabel("Easting")
    plt.ylabel("Northing")

    # Display the plot
    plt.show()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def analyze_traverse():
    file_path = file_entry.get()
    point1 = int(point1_entry.get())
    point2 = int(point2_entry.get())

    distance, bearing = calculate_traverse_characteristics(file_path, point1, point2)

    result_label.config(text=f"Distance: {distance:.2f}, Bearing: {bearing:.2f}")

    plot_traverse(file_path)

# Create tkinter window
window = tk.Tk()
window.title("Traverse Analysis")

# File selection
file_label = tk.Label(window, text="Traverse Data File:")
file_label.pack()

file_entry = tk.Entry(window, width=50)
file_entry.pack()

browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

# Point selection
point1_label = tk.Label(window, text="Point 1:")
point1_label.pack()

point1_entry = tk.Entry(window, width=10)
point1_entry.pack()

point2_label = tk.Label(window, text="Point 2:")
point2_label.pack()

point2_entry = tk.Entry(window, width=10)
point2_entry.pack()

# Analysis button
analyze_button = tk.Button(window, text="Analyze", command=analyze_traverse)
analyze_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the tkinter event loop
window.mainloop()