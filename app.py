from pathlib import Path
from shiny import App, ui, reactive, Session

from modules import map

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.link(rel="stylesheet", type="text/css", href="style.css"),
        ui.tags.script(src="index.js")
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
                ),
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
    ui.tags.div(map.map_ui("map"), id="map-container"),
    title="Respiratory Disease App",
)


def server(input, output, session: Session):
    @reactive.Effect
    @reactive.event(input.tab_map)
    async def _():
        await session.send_custom_message(
            "toggleActiveTab", {"activeTab": "map"}
        )

    @reactive.Effect
    @reactive.event(input.tab_plot)
    async def _():
        await session.send_custom_message(
            "toggleActiveTab", {"activeTab": "plot"}
        )

    map.map_server("map")


www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)
