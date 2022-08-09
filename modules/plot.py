from shiny import ui, module
from utils.sidebar_text import (
    about_text,
    slider_text_plot,
    dataset_information,
    missing_note,
)


@module.ui
def plot_ui():
    return ui.layout_sidebar(
        sidebar=ui.panel_sidebar(
            about_text,
            ui.tags.hr(),
            slider_text_plot,
            ui.tags.br(),
            ui.input_slider(
                id="years_value",
                label="Select Year",
                min=1990,
                max=2017,
                value=2010,
            ),
            ui.input_select(
                id="country_select",
                label="Select Countries:",
                choices=["One", "Two", "Three", "World"],
                selected="World",
                # multiple option does not work
            ),
            ui.tags.hr(),
            dataset_information,
            ui.tags.hr(),
            missing_note,
            class_="plot-sidebar",
        ),
        main="",
    )


@module.server
def plot_server(input, output, session):
    pass
