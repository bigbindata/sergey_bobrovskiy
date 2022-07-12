from typing import List

class TrafficLight():

  def __init__(self,position:int, duration_red:int, duration_green:int):
    self._position = position
    self._count_condition = [False]*duration_red + [True]*duration_green
    self._current_count_condition = 0
    self._colour = self._count_condition[self._current_count_condition]

  def change_condition(self):
    self._current_count_condition += 1
    if self._current_count_condition == len(self._count_condition):
      self._current_count_condition = 0
    self._colour = self._count_condition[self._current_count_condition]


  def can_go(self) -> bool:
    return self._colour

def Unmanned(L: int,N: int, track: List[List[int]]) -> int:
  if N >0:
    list_traffic_light_position = [params_traffic_light[0] for params_traffic_light in track]
    list_traffic_light = [TrafficLight(*params_traffic_light) for params_traffic_light in track]
    time_for_distance = 0
    distance = 0
    while distance != L:

      time_for_distance += 1
      if distance not in list_traffic_light_position:
        distance += 1
      else:
        if list_traffic_light[list_traffic_light_position.index(distance)].can_go():
          distance += 1

      for traffic_light in list_traffic_light:
        traffic_light.change_condition()
    return time_for_distance
  else:
    return L