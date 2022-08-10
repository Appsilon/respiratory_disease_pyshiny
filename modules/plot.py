import plotly.graph_objects as go
import plotly.express as px
from pandas import read_csv
from shiny import ui, module, reactive
from shinywidgets import (
    output_widget,
    render_widget,
)
from utils.helper_text import (
    about_text,
    slider_text_plot,
    dataset_information,
    missing_note,
)


data_oecd = read_csv("data/plot_data_oecd.csv")
data_world_bank = read_csv("data/plot_data_world_bank.csv")

country_choices = data_oecd["Entity"].unique().tolist() + ["World"]


@module.ui
def plot_ui():
    return ui.tags.div(
        ui.tags.div(
            about_text,
            ui.tags.hr(),
            slider_text_plot,
            ui.tags.br(),
            ui.input_slider(
                id="years_value",
                label="Select Year",
                min=1990,
                max=2017,
                value=[2010, 2015],
                sep="",
            ),
            ui.input_select(
                id="country_select",
                label="Select Countries:",
                choices=country_choices,
                selected="World",
                # multiple option does not work
            ),
            ui.tags.hr(),
            dataset_information,
            ui.tags.hr(),
            missing_note,
            class_="main-sidebar",
        ),
        ui.tags.div(
            output_widget("dr_plot"),
            ui.tags.hr(),
            output_widget("pm_plot"),
            class_="main-main",
        ),
        class_="main-layout",
    )


@module.server
def plot_server(input, output, session, is_wb_data):
    @reactive.Calc
    def data():
        if is_wb_data():
            return data_world_bank
        return data_oecd

    @reactive.Calc
    def fig_one():
        plot_data = data()[
            data()["Year"].between(
                input.years_value()[0], input.years_value()[1]
            )
        ]
        plot_data = plot_data[plot_data["Entity"] == input.country_select()]
        fig = px.line(
            data_frame=plot_data,
            x="Year",
            y="Death.Rate",
            color="Entity",
            title="Death Rate From Respiratory Diseases",
            labels={
                "Year": "Year",
                "Death.Rate": "Deaths per 100,000",
            },
        )
        return go.FigureWidget(fig)

    @reactive.Calc
    def fig_two():
        plot_data = data()[
            data()["Year"].between(
                input.years_value()[0], input.years_value()[1]
            )
        ]
        plot_data = plot_data[plot_data["Entity"] == input.country_select()]
        fig = px.line(
            data_frame=plot_data,
            x="Year",
            y="PM2.5",
            color="Entity",
            title="PM2.5 Measure",
        )
        return go.FigureWidget(fig)

    @output(suspend_when_hidden=False)
    @render_widget
    def dr_plot():
        return fig_one()

    @output(suspend_when_hidden=False)
    @render_widget
    def pm_plot():
        return fig_two()
