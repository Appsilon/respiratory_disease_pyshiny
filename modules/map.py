from typing import cast
from pandas import read_csv, DataFrame
from geopandas import read_file
from shiny import ui, module, reactive
from shinywidgets import output_widget, register_widget

from ipywidgets import Layout
from ipyleaflet import Map, LayerGroup, basemaps

from utils.helper_text import (
    about_text,
    missing_note,
    dataset_information,
    slider_text_map,
)
from utils.map_utils import add_circles, add_polygons, fiilter_data

basemap = cast(dict, basemaps)

map_data_world_bank = read_csv("data/map_data_world_bank.csv")
map_data_oecd = read_csv("data/map_data_oecd.csv")
polygon_data = read_file("data/countries.geojson")


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
    # Initialize and display when the session starts (1)
    map = Map(
        basemap=basemap["CartoDB"]["Positron"],
        center=(50, 10),
        zoom=5,
        scroll_wheel_zoom=True,
        min_zoom=3,
        max_zoom=18,
        no_wrap=True,
        layout=Layout(width="100%", height="100%"),
    )
    register_widget("map", map)

    # Circles Layer will later be filled with circleMarkers
    circles = LayerGroup()
    map.add_layer(circles)

    # Polygon layer will later be filled reactively
    polygons = LayerGroup()
    map.add_layer(polygons)

    @reactive.Calc
    def point_data() -> DataFrame:
        if is_wb_data():
            return fiilter_data(map_data_world_bank, input.years_value())
        return fiilter_data(map_data_oecd, input.years_value())

    @reactive.Effect
    def _():
        add_circles(point_data(), circles)  # pyright: ignore

    @reactive.Effect()
    def _():
        add_polygons(polygon_data, point_data(), polygons)  # pyright: ignore
