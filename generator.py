import osmnx as ox
import numpy as np
import random
from datetime import datetime, timezone


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

    rating = np.clip(random.gauss(4.3, 1), 0, 5) # большая часть рейтинга около 4 (я думаю)

    return time, from_node, to_node, round(route_len, 2), int(cost), int(rating)


if __name__ == '__main__':
    print(Generate_data())
