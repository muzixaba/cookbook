import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile
gdf = gpd.read_file("F:\CEMETERY_SHAPE\ITIS50V_CULT_PUBLIC_CEMETERY_polygon.shp")

# Display basic information about the shapefile
print(gdf.info())

# Display the first few rows of the data to get an idea of its structure
print(gdf.head())

# Display the number of polygons in the shapefile
print(f"Number of polygons: {len(gdf)}")

# Plot the shapefile to visualize the polygons
gdf.plot()
plt.title("Cemetery Polygons")
plt.show()
