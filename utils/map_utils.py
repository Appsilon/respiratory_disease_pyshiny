from pandas import DataFrame
from numpy import isnan
from ipyleaflet import Circle, LayerGroup


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
    return int(res * 10_000)


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
    for i in range(geodata.shape[0]):
        row = geodata.iloc[i, :]  # pyright: ignore
        circle = Circle()
        circle.name = "points"
        circle.location = (row.lat, row.lng)
        circle.weight = 1
        circle.radius = determine_circle_radius(row["Death.Rate"])
        circle.color = "white"
        circle.fill_color = determine_circle_color(row["PM2.5"])
        circle.fill_opacity = 0.5
        circle.opacity = 0.7
        circle_layer.add_layer(circle)
    return circle_layer
