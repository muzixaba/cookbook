def calculate_cemetery_area(coordinates):
    """
    Calculates the area of a polygon (representing a cemetery) given 8 coordinates
    using the shoelace formula and returns the area in hectares.

    Args:
        coordinates (list): A list of 8 tuples, where each tuple (x, y) represents
                            a coordinate of a vertex of the polygon. The coordinates
                            should be ordered sequentially around the perimeter.

    Returns:
        float: The area of the polygon in hectares. Returns None if the input
               does not contain exactly 8 coordinates.
    """
    if len(coordinates) != 8:
        print("Error: Please provide exactly 8 coordinates for the polygon.")
        return None

    n = len(coordinates)
    # Approximate conversion factor from degrees (latitude/longitude) to meters.
    # This is a rough approximation and varies significantly with latitude.
    # For accurate area calculations on spherical coordinates, a proper
    # geographic projection (e.g., UTM) or a geodesic library should be used.
    DEGREE_TO_METER_APPROX = 111000  # Roughly 111 km per degree

    # Convert input coordinates from degrees to approximate meters
    converted_coordinates = []
    for x_deg, y_deg in coordinates:
        converted_coordinates.append(
            (x_deg * DEGREE_TO_METER_APPROX, y_deg * DEGREE_TO_METER_APPROX)
        )

    area_sq_units = 0.0

    for i in range(n):
        x1, y1 = converted_coordinates[i]
        x2, y2 = converted_coordinates[
            (i + 1) % n
        ]  # Connects the last point to the first
        area_sq_units += x1 * y2 - x2 * y1

    area_sq_units = abs(area_sq_units) / 2.0

    # Convert square units (now in approximate square meters) to hectares
    # 1 hectare = 10,000 square meters
    area_hectares = area_sq_units / 10000.0

    return area_hectares


# Example Usage (assuming coordinates are in meters):
if __name__ == "__main__":
    # Example 1: A simple rectangle (for testing)
    # Area = 100m * 50m = 5000 sq meters = 0.5 hectares
    coords = [
        (-27.656199147530913, 30.327611513795336),
        (-27.656683717180144, 30.327946715646238),
        (-27.657157080833137, 30.328285079778748),
        (-27.656826566778957, 30.329591102083572),
        (-27.656582882050856, 30.330615681325945),
        (-27.6560478941335, 30.330463891808556),
        (-27.65556052066316, 30.330334238262452),
        (-27.655888237546286, 30.328964970324350),
    ]

    area1 = calculate_cemetery_area(coords)
    if area1 is not None:
        print(f"The area of the cemetery (octagon example) is: {area1:.4f} hectares")
