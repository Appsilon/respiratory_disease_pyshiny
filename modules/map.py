import random
import json
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


def determine_circle_radius(num):
    """Logic from the original app"""
    res = 0
    if num < 10:
        res = num * 0.75
    elif num > 25:
        res = num * 0.25
    elif num > 0.5:
        res = num * 0.2
    else:
        res = num * 0.1
    return int(res * 10_000)


@module.ui
def map_ui():
    return ui.tags.div(
        ui.tags.div(
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
            class_="main-sidebar card-style",
        ),
        ui.tags.div(
            output_widget("map", width="auto", height="auto"),
            class_="main-main card-style no-padding",
        ),
        class_="main-layout",
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
    circles = L.LayerGroup()

    map.add_layer(circles)

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

        # remove layers first
        circles.clear_layers()

        for i in range(point_data().shape[0]):
            row = point_data().iloc[i, :]  # pyright: ignore
            circle = L.Circle()
            circle.name = "points"
            circle.location = (row.lat, row.lng)
            circle.weight = 1
            circle.radius = determine_circle_radius(row["Death.Rate"])
            circle.color = "white"
            circle.fill_color = "green"  # TODO: add palette
            circle.fill_opacity = 0.5
            circle.opacity = 0.7
            circles.add_layer(circle)

    register_widget("map", map)
