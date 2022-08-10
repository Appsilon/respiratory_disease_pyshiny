import random
import json
import geopandas
from pandas import read_csv
from shiny import ui, module, reactive
from shinywidgets import output_widget, register_widget

from ipywidgets import Layout
import ipyleaflet as L

from utils.helper_text import (
    about_text,
    missing_note,
    dataset_information,
    slider_text_map,
)

map_data_world_bank = read_csv("data/map_data_world_bank.csv")
map_data_oecd = read_csv("data/map_data_oecd.csv")

with open("data/countries.geojson", "r") as f:
    data = json.load(f)


def random_color(feature):
    return {
        "color": "black",
        "fillColor": random.choice(["red", "yellow", "green", "orange"]),
    }


@module.ui
def map_ui():
    return ui.layout_sidebar(
        sidebar=ui.panel_sidebar(
            about_text,
            ui.tags.hr(),
            slider_text_map,
            ui.tags.br(),
            ui.input_slider(
                id="years_value",
                label="Select Year",
                min=1990,
                max=2017,
                value=2010,
            ),
            ui.tags.hr(),
            dataset_information,
            ui.tags.hr(),
            missing_note,
            class_="plot-sidebar",
        ),
        main=ui.panel_main(output_widget("map", width="100%", height="85vh")),
    )


@module.server
def map_server(input, output, session, is_wb_data):
    @reactive.Calc
    def point_data():
        if is_wb_data():
            return map_data_world_bank[
                map_data_world_bank.Year == input.years_value()
            ]
        return map_data_oecd[map_data_oecd.Year == input.years_value()]

    # Initialize and display when the session starts (1)
    map = L.Map(
        # TODO: this is how it's done in tutorial :)
        basemap=L.basemaps.CartoDB.Positron,  # pyright: ignore
        center=(50, 10),
        zoom=5,
        scroll_wheel_zoom=True,
        min_zoom=3,
        max_zoom=18,
        no_wrap=True,
        layout=Layout(width="100%", height="100%"),
    )
    geo_json = L.GeoJSON(
        data=data,
        style={
            "opacity": 1,
            "dashArray": "9",
            "fillOpacity": 0.1,
            "weight": 1,
        },
        hover_style={
            "color": "black",
            "weight": 2,
            "dashArray": "0",
            "fillOpacity": 0.5,
        },
        name="polygons",
        style_callback=random_color,
    )
    map.add_layer(geo_json)

    @reactive.Effect
    def _():
        # TODO: remove points layer in a proper way
        if len(map.layers) > 2:
            map.remove_layer(map.layers[2])
        gdf = geopandas.GeoDataFrame(
            data=point_data(),
            geometry=geopandas.points_from_xy(  # pyright: ignore
                point_data().lng, point_data().lat
            ),
        )
        geo_data = L.GeoData(
            geo_dataframe=gdf,
            style={
                "color": "black",
                "radius": 8,
                "fillColor": "#3366cc",
                "opacity": 0.5,
                "weight": 1.9,
                "dashArray": "2",
                "fillOpacity": 0.6,
            },
            hover_style={"fillColor": "red", "fillOpacity": 0.2},
            point_style={
                "radius": 5,
                "color": "red",
                "fillOpacity": 0.8,
                "fillColor": "blue",
                "weight": 3,
            },
            name="points",
        )
        map.add_layer(geo_data)

    register_widget("map", map)
