from collections import deque

class ConditionProgrammDeque():

    def __init__ (self, list_string_condition, position, last_command):
        self._deque_string_condition = deque(list_string_condition)
        self._position = position
        self._last_command = last_command
        self._count_use_undo = 0
        self._count_use_append_or_del = 0


    def get_count_use_undo(self,):
        return self._count_use_undo

    def set_count_use_undo(self, value):
        self._count_use_undo = value

    def increment_count_use_undo(self,):
        self._count_use_undo += 1
    
    def decrement_count_use_undo(self,):
        self._count_use_undo -= 1

    def get_count_use_append_or_del(self,):
        return self._count_use_append_or_del

    def set_count_use_append_or_del(self, value):
        self._count_use_append_or_del = value

    def increment_count_use_append_or_del(self,):
        self._count_use_append_or_del += 1

    def decrement_count_use_append_or_del(self,):
        self._count_use_append_or_del -= 1

    def get_position(self,):
        return self._position
    
    def set_position(self, value):
        self._position = value
 
    def increment_position(self,):
        self._position += 1
        self._deque_string_condition.rotate(1)
        

    def decrement_position(self,):
        self._position -= 1
        self._deque_string_condition.rotate(-1)


    def set_list_string_condition(self, value):
        self._deque_string_condition = deque(value)

    def get_list_string_condition(self,):
        return self._deque_string_condition
    
    def append_to_string_condition(self, value):
        self._deque_string_condition.append(value)
    
    def get_current_string_condition(self,):
        return self._deque_string_condition[0]
    
    def set_last_command(self, value):
        self._last_command = value
    
    def get_last_command(self):
        return self._last_command


def append_string(S: str) -> str:
    global global_string
    if condition_programm.get_count_use_undo()>0:
        condition_programm.set_position(0)
        condition_programm.set_list_string_condition([global_string, ])
        condition_programm.set_count_use_undo(0)
        condition_programm.set_count_use_append_or_del(0)

    condition_programm.append_to_string_condition(condition_programm.get_current_string_condition() + S)

    condition_programm.increment_position()
    condition_programm.set_last_command(1)
    condition_programm.increment_count_use_append_or_del()

    global_string = condition_programm.get_current_string_condition()
    return global_string


def del_symbols(N:str) -> str:
    global global_string
    N = int(N)

    if condition_programm.get_count_use_undo()>0:
        condition_programm.set_position(0)
        condition_programm.set_list_string_condition([global_string, ])
        condition_programm.set_count_use_undo(0)
        condition_programm.set_count_use_append_or_del(0)

    if N >= len(global_string):
        condition_programm.append_to_string_condition("")
    else:
        condition_programm.append_to_string_condition(global_string[:-N])

    condition_programm.increment_position()
    condition_programm.set_last_command(2)
    condition_programm.increment_count_use_append_or_del()


    global_string = condition_programm.get_current_string_condition()
    return global_string


def return_symbol_by_index(i:str) -> str:
    global global_string
    i = int(i)
    condition_programm.set_last_command(3)
    if i > len(global_string)-1:
        return ""
    return global_string[i]


def Undo():
    global global_string

    if condition_programm.get_last_command() in (1, 2, 4, 5) and condition_programm.get_count_use_append_or_del() > 0:
        condition_programm.decrement_position()
        condition_programm.decrement_count_use_append_or_del()
        global_string = condition_programm.get_current_string_condition()
    condition_programm.set_last_command(4)
    condition_programm.increment_count_use_undo()
    
    return global_string


def Redo():
    global global_string

    if condition_programm.get_last_command() in (4, 5) and condition_programm.get_count_use_undo() > 0:
        condition_programm.increment_position()
        condition_programm.decrement_count_use_undo()
        global_string = condition_programm.get_current_string_condition()
        condition_programm.increment_count_use_append_or_del()

    condition_programm.set_last_command(5)
    return global_string


def BastShoe(command: str) -> str:
    global global_string
    dict_function = {"1": append_string,
                 "2": del_symbols,
                 "3": return_symbol_by_index,
                 "4": Undo,
                 "5": Redo,}

    number_command = command[0]
    arguments = command[2:]
    
    if number_command in ("4", "5"):
        dict_function[number_command]()
        return global_string

    elif number_command == "3":
        return dict_function[number_command](arguments)
        
    else:
        dict_function[number_command](arguments)
        return global_string


global_string = ""
condition_programm = ConditionProgrammDeque(["",],0, None)
