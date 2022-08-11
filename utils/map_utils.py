from pandas import DataFrame
from numpy import isnan
from ipyleaflet import CircleMarker, LayerGroup


def determine_circle_radius(num: float) -> int:
    """Circles are scaled differently in ipyleaflet compared to R/Leaflet,
    hence different coefficients.
    """
    num = int(num)

    bins = [range(10), range(10, 20), range(20, 25)]
    coefficients = [1.1, 0.8, 0.75]
    final_coef = 0.2

    for bin, coef in zip(bins, coefficients):
        if num in bin:
            return int(num * coef)
    return int(num * final_coef)


def determine_circle_color(num: float) -> str:
    if isnan(num):
        return "#D2D2D2"
    num = int(num)

    bins = [
        range(1),
        range(1, 2),
        range(2, 5),
        range(5, 10),
        range(10, 20),
        range(20, 50),
        range(50, 100),
    ]
    colors = [
        "#F7FCF0",
        "#E0F3DB",
        "#CCEBC5",
        "#A8DDB5",
        "#7BCCC4",
        "#4EB3D3",
        "#2B8CBE",
    ]
    final_color = "#08589E"

    for bin, color in zip(bins, colors):
        if num in bin:
            return color
    return final_color


def add_circles(geodata: DataFrame, circle_layer: LayerGroup) -> None:
    """Layer data is updated by reference, hence None return"""
    circle_layer.clear_layers()
    circle_markers = []
    for _, row in geodata.iterrows():
        popup = HTML(
            f"<b>{row.Entity}:</b></br>" + str(round(row["Death.Rate"], 2))
        )
        circle_marker = CircleMarker(
            location=[row["lat"], row["lng"]],
            radius=determine_circle_radius(row["Death.Rate"]),
            weight=1,
            color="white",
            opacity=0.7,
            fill_color=determine_circle_color(row["Death.Rate"]),
            fill_opacity=0.5,
            popup=popup,
        )
        circle_markers.append(circle_marker)
    points = LayerGroup(layers=circle_markers)
    circle_layer.add_layer(points)
