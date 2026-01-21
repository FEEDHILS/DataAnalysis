import osmnx as ox
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import random
from datetime import datetime, timezone
import time

# Скачиваем бОльшую часть Владивостока
print("Загрузка графа")
Vladivostok = ox.graph.graph_from_bbox([131.84040, 43.07165, 132.00176, 43.13958], network_type='drive')
print("Граф города готов к использованию")


cost_per_meter = 1/10
def Generate_data():
    from_node = list(Vladivostok.nodes)[random.randint(0, Vladivostok.number_of_nodes()-1 )]
    to_node = list(Vladivostok.nodes)[random.randint(0, Vladivostok.number_of_nodes()-1 )]
    route = ox.routing.shortest_path(Vladivostok, from_node, to_node)

    # Иногда может получиться что невозможно построить маршрут для двух случайных точек
    if route is None:
        return Generate_data()
    
    # складываем грани меж точек нашего маршрута
    route_len = sum(ox.routing.route_to_gdf(Vladivostok, route)['length'])
    time = datetime.now(timezone.utc)

    # небольшой рандом для цены
    coeff = random.random()*cost_per_meter - cost_per_meter/2
    cost = route_len * (cost_per_meter + coeff)

    rating = int( np.clip(random.gauss(4.3, 1), 0, 5) ) # большая часть рейтинга около 4
    return time, from_node, to_node, int(route_len), int(cost), rating



while True:
    data = Generate_data()
    print(data)
    time.sleep(2)
