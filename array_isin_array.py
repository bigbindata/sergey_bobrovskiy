from typing import List

def return_index_substring(substring: str, string:str) -> List[str]:
  list_start_i = []
  for i in range(0,len(string)):
    if substring == string[i:i+len(substring)]:
      list_start_i.append(i)
  return list_start_i

def TankRush(H1: int, W1: int, S1: str,H2: int, W2: int, S2:str) -> bool:
  maps = S1.split()
  tanks = S2.split()
  list_coordinates = []
  for indexs1, string_s1 in enumerate(maps):
    if tanks[0] in string_s1 and indexs1+H2 <= H1:
      list_coordinates += [(indexs1,i) for i in return_index_substring(tanks[0], string_s1)]
    if not list_coordinates:
      return False
  for coordinates in list_coordinates:
      border_w = coordinates[1]+W2
      border_h = coordinates[0]+H2
      if "".join(tanks)=="".join([i[coordinates[1]:border_w] for i in maps[coordinates[0]:border_h]]):
        return True
  return False



