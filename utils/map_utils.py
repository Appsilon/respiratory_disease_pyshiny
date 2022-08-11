from pandas import DataFrame
from numpy import isnan
from ipyleaflet import CircleMarker, LayerGroup


def determine_circle_radius(num):
    """Logic from the original app"""
    res = 0
    if num < 10:
        res = num * 0.75
    elif num > 25:
        res = num * 0.25
    elif num > 0.5:
        res = num * 0.2
    else:
        res = num * 0.1
    return int(res)


def determine_circle_color(num):
    if isnan(num):
        color = "#D2D2D2"
    elif num < 1:
        color = "#F7FCF0"
    elif num < 2:
        color = "#E0F3DB"
    elif num < 5:
        color = "#CCEBC5"
    elif num < 10:
        color = "#A8DDB5"
    elif num < 20:
        color = "#7BCCC4"
    elif num < 50:
        color = "#4EB3D3"
    elif num < 100:
        color = "#2B8CBE"
    else:
        color = "#08589E"
    return color


def add_circles(geodata: DataFrame, circle_layer: LayerGroup):
    circle_layer.clear_layers()
    circle_markers = []
    for _, row in geodata.iterrows():
        circle_marker = CircleMarker(
            location=[row["lat"], row["lng"]],
            radius=determine_circle_radius(row["Death.Rate"]),
            weight=1,
            color="white",
            opacity=0.7,
            fill_color=determine_circle_color(row["Death.Rate"]),
            fill_opacity=0.5,
        )
        circle_markers.append(circle_marker)
    points = LayerGroup(layers=circle_markers)
    circle_layer.add_layer(points)
