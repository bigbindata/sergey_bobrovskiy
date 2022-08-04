from collections import deque
from typing import List

def return_dict_with_deque(original,height_matrix,weight_matrix):

    lower_index = 0
    right_index = 0
    dict_with_deque = {}
    for index_height in range(height_matrix):
        if height_matrix/2 == index_height: 
            break

        upper_index = left_index = index_height

        lower_index -= 1
        right_index -= 1
        
        left_vertical_array = [ ]
        right_vertical_array = [ ]
        mini_matrix = original[index_height:]  


        if index_height != 0:
            mini_matrix = original[index_height:lower_index+1]

        for index, array in enumerate(mini_matrix):
            if index == 0:
                upper_horizontal_array = array[left_index+1:right_index]
            if index == len(mini_matrix) - 1:
                lower_horizontal_array = array[::-1][left_index+1:right_index]
            left_vertical_array.insert(0,array[left_index])
            right_vertical_array.append(array[right_index])

        level_list = left_vertical_array + upper_horizontal_array + right_vertical_array + lower_horizontal_array

        deque_line = deque(level_list)
        deque_line.rotate()
        dict_with_deque[index_height] = {}
        dict_with_deque[index_height]["deque"] = deque_line
        dict_with_deque[index_height]["len_left"] = len(left_vertical_array)
        dict_with_deque[index_height]["len_right"] = len(right_vertical_array)
        dict_with_deque[index_height]["len_upper"] = len(upper_horizontal_array)
        dict_with_deque[index_height]["len_lower"] = len(lower_horizontal_array)

    return dict_with_deque

def return_all_array(values):
    example = list(values['deque'])
    left_array = example[:values['len_left']]
    upper_array = example[values['len_left'] : values['len_left'] + values['len_upper']]
    lower_array = example[-values['len_lower']:]
    lower_array.reverse()
    right_array = example[-values['len_lower'] - values['len_right']:-values['len_lower'] ]

    full_upper_array = [left_array[-1]] + upper_array + [right_array[0]]
    full_lower_array = [left_array[0]] + lower_array + [right_array[-1]]
    clear_left_array = left_array[1:-1]
    clear_right_array = right_array[1:-1]
    return {"up":full_upper_array,
            "down":full_lower_array,
            "left":clear_left_array,
            "right":clear_right_array}

def return_matrix(dict_array_func, matrix):
    

    for index, array in enumerate(matrix):
        if index != 0 or index != len(matrix) - 1:
            array.insert(0, dict_array_func['left'][::-1][index - 1])
            array.append( dict_array_func['right'][index - 1])
    matrix.insert(0, dict_array_func['up'])
    matrix.append(dict_array_func['down'])
    return matrix

def rotate_matrix_one_time(original, height_matrix, weight_matrix):
    original = [list(i) for i in original]
    
    dict_with_deque = return_dict_with_deque(original, height_matrix=height_matrix, weight_matrix=weight_matrix)

    for index_dict_with_deque in sorted(dict_with_deque.keys(),reverse=True):
        dict_array = return_all_array(dict_with_deque[index_dict_with_deque])
        if not dict_array["left"]:
            full_matrix = [dict_array["up"], dict_array["down"]]
        else:
            full_matrix = return_matrix(dict_array, full_matrix)
    return full_matrix

def MatrixTurn(Matrix:List[str], M:int, N:int, T:int) -> None:
    for _ in range(T):
        Matrix = rotate_matrix_one_time(Matrix, M, N)
        Matrix = ["".join(i) for i in Matrix]