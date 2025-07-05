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
        (-30.786511989953905, 30.402168557588567),
        (-30.787541091082275, 30.403996956488903),
        (-30.788182016921358, 30.405121316732217),
        (-30.790529032824647, 30.402609895254162),
        (-30.79193721486819, 30.400855052631428),
        (-30.791630305154833, 30.40028761848994),
        (-30.79139583577517, 30.398292872905962),
        (-30.78902153303685, 30.400739464195194),
    ]

    area1 = calculate_cemetery_area(coords)
    if area1 is not None:
        print(f"The area of the cemetery (octagon example) is: {area1:.4f} hectares")
