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
from utils.map_utils import add_circles


map_data_world_bank = read_csv("data/map_data_world_bank.csv")
map_data_oecd = read_csv("data/map_data_oecd.csv")


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
    register_widget("map", map)

    # Circles Layer will later be filled with circleMarkers
    circles = L.LayerGroup()
    map.add_layer(circles)

    @reactive.Calc
    def point_data():
        if is_wb_data():
            return map_data_world_bank[
                map_data_world_bank.Year == input.years_value()
            ]
        return map_data_oecd[map_data_oecd.Year == input.years_value()]

    @reactive.Effect
    def _():
        add_circles(point_data(), circles)  # pyright: ignore
