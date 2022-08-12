import plotly.graph_objects as go
import plotly.express as px
from pandas import DataFrame


def create_figure(
    data: DataFrame,
    year_range: list[int],
    country: str,
    y_from: str,
    title: str,
    labels: dict,
) -> go.FigureWidget:
    plot_data = data[data["Year"].between(year_range[0], year_range[1])]
    plot_data = plot_data[plot_data["Entity"] == country]

    fig = px.line(
        data_frame=plot_data,
        x="Year",
        y=y_from,
        color="Entity",
        title=title,
        labels=labels,
    )

    return go.FigureWidget(fig)
