import random
import json
from shiny import ui, module
from shinywidgets import output_widget, register_widget

from ipywidgets import Layout
import ipyleaflet as L

from utils.sidebar_text import (
    about_text,
    missing_note,
    dataset_information,
    slider_text_map,
)


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
def map_server(input, output, session):
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
        hover_style={"color": "white", "dashArray": "0", "fillOpacity": 0.5},
        style_callback=random_color,
    )
    # Add a distance scale
    map.add_layer(geo_json)
    register_widget("map", map)
