from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer

from money_model import MoneyModel


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 10:
        portrayal["Color"] = "#66d9ff"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.8
    elif agent.wealth > 8:
        portrayal["Color"] = "#66ffd9"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.6
    elif agent.wealth > 6:
        portrayal["Color"] = "#66ff66"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
    elif agent.wealth > 4:
        portrayal["Color"] = "#b3ff66"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.4
    elif agent.wealth > 2:
        portrayal["Color"] = "#ffff66"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.3
    elif agent.wealth > 0:
        portrayal["Color"] = "#ffd966"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    else:
        portrayal["Color"] = "#ff8c66"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.1
    return portrayal

grid = CanvasGrid(agent_portrayal, 2, 2, 500, 500)
chart = ChartModule([
    {"Label": "Gini", "Color": "Black"}],
    data_collector_name='datacollector'
)

server = ModularServer(MoneyModel, [grid, chart], "Money Model", 100, 2, 2)
server.port = 8521
server.launch()
