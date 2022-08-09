import plotly.graph_objects as go
from shiny import ui, module
from shinywidgets import (
    output_widget,
    render_widget,
    register_widget,
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
            output_widget("dr_plot", width="100%", height="300px"),
            ui.tags.hr(),
            output_widget("pm_plot", width="100%", height="300px"),
        ),
    )


@module.server
def plot_server(input, output, session):

    trace = go.Heatmap(
        z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
        x=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        y=["Morning", "Afternoon", "Evening"],
    )
    data = [trace]
    layout = go.Layout(title="Activity Heatmap")

    f1 = go.FigureWidget(data, layout)
    f2 = go.FigureWidget(data, layout)

    # TODO: none of these methods work to display the plot
    register_widget("dr_plot", f1)

    @output
    @render_widget
    def pm_plot():
        return f2
