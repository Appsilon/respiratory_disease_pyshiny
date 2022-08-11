from pandas import DataFrame, read_csv
from geopandas import read_file


polygon_data = read_file("data/countries.geojson", crs=4326)
centroid = polygon_data.geometry.centroid
points_from_polygons = DataFrame(
    {
        "Code": polygon_data["id"],
        "lng": centroid.x,
        "lat": centroid.y,
    }
)

map_data_world_bank = (
    read_csv("data/map_data_world_bank.csv")
    .drop(["lng", "lat"], axis=1)
    .merge(points_from_polygons, on="Code")
)
map_data_oecd = (
    read_csv("data/map_data_oecd.csv")
    .drop(["lng", "lat"], axis=1)
    .merge(points_from_polygons, on="Code")
)
