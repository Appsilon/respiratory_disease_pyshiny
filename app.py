from pathlib import Path
from shiny import App, ui

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.link(rel="stylesheet", type="text/css", href="style.css")
    ),
    # top navbar
    ui.tags.div(
        ui.row(
            ui.column(
                2,
                ui.tags.div(
                    ui.tags.a(
                        ui.tags.img(
                            src="static/img/appsilon-logo.png", height="50px"
                        ),
                        href="https://demo.appsilon.com/",
                    ),
                    id="logo-top",
                )
            ),
            ui.column(2),
            ui.column(
                2,
                ui.tags.div(
                    ui.tags.div(
                        ui.input_action_button(
                            id="tab_map",
                            label="Map",
                            class_="navbar-button",
                        ),
                        id="div-navbar-map",
                    ),
                    ui.tags.div(
                        ui.input_action_button(
                            id="tab_plot",
                            label="Graphs",
                            class_="navbar-button",
                        ),
                        id="div-navbar-plot",
                    ),
                    id="div-navbar-tabs",
                ),
            ),
            ui.column(3),
            ui.column(
                2,
                ui.tags.div(
                    ui.input_switch(
                        id="dataset", label="Dataset Select", value=True
                    ),
                    id="div-navbar-selector",
                ),
            ),
            ui.column(
                1,
                ui.tags.div(
                    ui.input_action_button(
                        id="info_icon",
                        label=None,
                        icon="circle",  # TODO: how to make an icon?
                        class_="navbar-info",
                    )
                ),
            ),
        ),
        id="div-navbar",
        class_="navbar-top",
    ),
    # main area
    ui.output_ui("display_area"),
    title="Respiratory Disease App",
)


def server(input, output, session):
    pass


www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)
