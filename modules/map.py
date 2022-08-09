from shiny import ui, module
from shinywidgets import output_widget, register_widget

from ipywidgets import Layout
import ipyleaflet as L


@module.ui
def map_ui():
    return ui.layout_sidebar(
        sidebar=ui.panel_sidebar(
            ui.tags.h3("About"),
            ui.tags.br(),
            ui.tags.p(
                """
                The app gives a visual overview of PM2.5 air pollution
                for different
                countries over the years and its potential relationship
                to respiratory
                diseases and their prevalence.
                """,
                style="""
                text-align: justify;
                word-break:break-word;
                hyphens: auto;
                """,
            ),
            ui.tags.hr(),
            ui.tags.p(
                """
                Please use the slider below to choose the year. The map will
                reflect data for the input""",
                style="""
                    text-align: justify;
                    word-break:break-word;
                    hyphens: auto;
                """,
            ),
            ui.tags.br(),
            ui.input_slider(
                id="years_value",
                label="Select Year",
                min=1990,
                max=2017,
                value=2010,
            ),
            ui.tags.hr(),
            ui.tags.strong(ui.tags.h3("Dataset Information")),
            ui.tags.p(
                """
                For the app, we have chosen data from the World Bank and
                Organisation for Economic Co-operation and Development (OECD).
                Also, for the data regarding the Death Rate, we relied on
                Our World in Data. References
                to all three can be found below.
                """,
                style="""
                    text-align: justify;
                    word-break:break-word;
                    hyphens: auto;
                """,
            ),
            ui.tags.ul(
                ui.tags.li(
                    ui.tags.a(
                        "World Bank",
                        href=(
                            "https://data.worldbank.org/indicator/"
                            + "EN.ATM.PM25.MC.M3"
                        ),
                    )
                ),
                ui.tags.li(
                    ui.tags.a(
                        "OECD",
                        href=(
                            "https://stats.oecd.org/"
                            + "Index.aspx?DataSetCode=EXP_PM2_5"
                        ),
                    )
                ),
                ui.tags.li(
                    ui.tags.a(
                        "Our World in Data",
                        href=(
                            "https://ourworldindata.org/"
                            + "grapher/respiratory-disease-death-rate"
                        ),
                    )
                ),
            ),
            ui.tags.hr(),
            ui.tags.p(
                ui.tags.strong("Note: "),
                """
                    For years 1990 to 2010, the PM2.5 data was collected
                    at every
                    five-year mark. That is, the PM2.5 data is only
                    available for
                    1990, 1995, 2000, 2005, 2010, and 2010 onwards.
                """,
                style="""
                    font-size: 14px;
                    text-align: justify;
                    word-break:break-word;
                    hyphens: auto;
                """,
            ),
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
        center=(51.476852, -0.000500),
        zoom=12,
        scroll_wheel_zoom=True,
        min_zoom=3,
        max_zoom=18,
        no_wrap=True,
        layout=Layout(width="100%", height="100%"),
    )
    # Add a distance scale
    map.add_control(L.leaflet.ScaleControl(position="bottomleft"))
    register_widget("map", map)
