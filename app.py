from pathlib import Path
from shiny import App, ui

app_ui = ui.page_fluid(
    # top navbar
    ui.tags.div(
        ui.row(
            ui.column(
                2,
                ui.tags.div(
                    ui.tags.a(
                        ui.tags.img(
                            src="static/img/appsilon-logo.png",
                            height="50px"
                        ),
                        href="https://demo.appsilon.com/"
                    ),
                    id="logo-top"
                )
            ),
            ui.column(2),
            ui.column(
                2,
                ui.tags.div(
                    id="div-navbar-tabs"
                )
            )
        ),
        id="div-navbar",
    ),
    title="Respiratory Disease App",
)


def server(input, output, session):
    pass


www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)
