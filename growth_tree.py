from typing import List
from copy import deepcopy

class Branch():
    def __init__(self, age, position_height, position_width ):
        self._age = age
        self._position_height = position_height
        self._position_width = position_width
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value

    @property
    def positions(self):
        return {"height":self._position_height,
                "width":self._position_width}

def set_branch(position_height, position_width):
    return Branch(1, position_height, position_width)


def return_array_start_tree(tree):
    list_start_tree = []
    for index_height, string in enumerate(tree):
        list_start_tree.append([])
        for index_width, symbol in enumerate(string):
            if symbol == "+":
                list_start_tree[index_height].append(Branch(1, index_height, index_width))
            else:
                list_start_tree[index_height].append(False)

    return list_start_tree


def _in_range(index,array_with_index):
    if 0 <= index <= len(array_with_index) - 1:
        return True
    return False


def a_year_has_passed(array_tree, number_year):
    a_year_pass_array = deepcopy(array_tree)
    a_year_pass_delete = []
    if number_year % 2 == 0:
        a_year_pass_delete = deepcopy(array_tree)

    for index_height, level in enumerate(array_tree):
        for index_width, position in enumerate(level):
            if position:
                a_year_pass_array[index_height][index_width].age += 1
                if a_year_pass_delete and a_year_pass_array[index_height][index_width].age >= 3:
                    a_year_pass_delete[index_height][index_width] = False

                    if _in_range(index_height + 1, array_tree):
                        a_year_pass_delete[index_height + 1][index_width] = False

                    if _in_range(index_height - 1, array_tree):
                        a_year_pass_delete[index_height - 1][index_width] = False

                    if _in_range(index_width + 1, level):
                        a_year_pass_delete[index_height][index_width + 1] = False

                    if _in_range(index_width - 1, level):
                        a_year_pass_delete[index_height][index_width - 1] = False
            else:
                a_year_pass_array[index_height][index_width] = set_branch(index_height, index_width)
    if a_year_pass_delete:
        return a_year_pass_delete
    return a_year_pass_array


def TreeOfLife(H:int, W:int, N: int, tree: List[str]) -> List[str]:
    array_tree = return_array_start_tree(tree)

    for year in range(1,N+1):
        array_tree =  a_year_has_passed(array_tree, year)

    return ["".join(map(lambda x: "+" if x else ".", level)) for level in array_tree]
    