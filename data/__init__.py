from pandas import read_csv
import os

for file in os.walk('.'):
    if "data" in file[0]:
        data_path = file[0]
        break

polygon_data = read_csv(f"{data_path}/countries.csv")
polygon_data["coordinates"] = polygon_data["coordinates"].apply(eval)
points_from_polygons = read_csv(f"{data_path}/points_from_polygons.csv")

map_data_world_bank = (
    read_csv(f"{data_path}/map_data_world_bank.csv")
    .drop(["lng", "lat"], axis=1)
    .merge(points_from_polygons, on="Code")
)
map_data_oecd = (
    read_csv(f"{data_path}/map_data_oecd.csv")
    .drop(["lng", "lat"], axis=1)
    .merge(points_from_polygons, on="Code")
)

plot_data_world_bank = read_csv(f"{data_path}/plot_data_world_bank.csv")
plot_data_oecd = read_csv(f"{data_path}/plot_data_oecd.csv")
