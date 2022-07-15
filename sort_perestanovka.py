from typing import List

class ImposibleSortList(Exception):
  def __init__(self, message):
    self.message = message

  def __str__(self):
    return self.message


def return_list_with_left_offset(old_list_for_offset: List) -> List:
  return old_list_for_offset[1:] + old_list_for_offset[:1]


def return_sorted_list(old_list):
    
  new_list=old_list.copy()
  count_operation = 0
  while sorted(old_list) != new_list:
    if count_operation == 3:
      raise  ImposibleSortList(f"{old_list} нельзя отсортировать по возрастанию")
    count_operation +=1
    new_list = return_list_with_left_offset(new_list)
  return new_list


def return_new_list_with_new_max(list_for_analysis_max):
  if max(list_for_analysis_max) == list_for_analysis_max[-1]:
    return list_for_analysis_max[:-1]

  else:
    return list_for_analysis_max


def return_list_with_3_elements_for_sort_and_max_value_index(list_for_3_elemets):
  index_max_element =  max([i for i, value in enumerate (list_for_3_elemets) if value == max(list_for_3_elemets)])
  return list_for_3_elemets[index_max_element - 1: index_max_element + 2], index_max_element


def return_new_example_list_with_better_sort(example_list):
  new_list_with_new_max = return_new_list_with_new_max(example_list)
  while new_list_with_new_max != return_new_list_with_new_max(new_list_with_new_max):
    new_list_with_new_max = return_new_list_with_new_max(new_list_with_new_max)

  new_list_for_sort, index_max_element = return_list_with_3_elements_for_sort_and_max_value_index(new_list_with_new_max)
  new_sorted_list = example_list[:index_max_element - 1] + return_sorted_list(new_list_for_sort) + example_list[index_max_element + 2: ]
  return new_sorted_list


def MisterRobot(N:int, data:List[int]) -> bool:
  try:
    sort_example_list = return_new_example_list_with_better_sort(data)

    while sort_example_list != sorted(data):
      sort_example_list = return_new_example_list_with_better_sort(sort_example_list)
    return True

  except ImposibleSortList:
    return False