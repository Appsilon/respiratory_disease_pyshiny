import plotly.graph_objects as go
from shiny import ui, module
from shinywidgets import (
    output_widget,
    render_widget,
)
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
        main=ui.panel_main(
            output_widget("dr_plot"),
            ui.tags.hr(),
            output_widget("pm_plot"),
        ),
    )


@module.server
def plot_server(input, output, session):

    fig_one = go.FigureWidget().add_scatter(x=[1, 2, 3], y=[10, 11, 12])
    fig_one.layout.title = "Figure One"  # pyright: ignore
    fig_two = go.FigureWidget().add_scatter(x=[1, 2, 3], y=[12, 11, 10])
    fig_two.layout.title = "Figure Two"  # pyright: ignore

    @output(suspend_when_hidden=False)
    @render_widget
    def dr_plot():
        return fig_one

    @output(suspend_when_hidden=False)
    @render_widget
    def pm_plot():
        return fig_two
