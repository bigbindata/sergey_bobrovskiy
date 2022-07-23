class ConditionProgrammList():

    def __init__ (self, list_string_condition, position, last_command):
        self._list_string_condition = list_string_condition
        self._position = position
        self._last_command = last_command
        self._count_use_undo = 0
        self._count_use_append_or_del = 0

    @property
    def count_use_undo(self,):
        return self._count_use_undo

    @count_use_undo.setter
    def count_use_undo(self, value):
        self._count_use_undo = value
        if self._count_use_undo < 0:
            self._count_use_undo = 0

    @property
    def count_use_append_or_del(self,):
        return self._count_use_append_or_del

    @count_use_append_or_del.setter
    def count_use_append_or_del(self, value):
        self._count_use_append_or_del = value
        if self._count_use_append_or_del < 0:
            self._count_use_append_or_del = 0

    @property
    def position(self,):
        return self._position
    
    @position.setter
    def position(self, value):
        self._position = value
        if self._position < 0:
            self._position = 0
        if self._position > len(self._list_string_condition) - 1:
            self._position = len(self._list_string_condition) - 1

    @property
    def list_string_condition(self,):
        return self._list_string_condition

    @list_string_condition.setter
    def list_string_condition(self, value):
        self._list_string_condition = list(value)
  
    def append_to_string_condition(self, value):
        self._list_string_condition.append(value)

    @property
    def current_string_condition(self,):
        return self._list_string_condition[self._position]
    
    @property
    def last_command(self):
        return self._last_command

    @last_command.setter
    def last_command(self, value):
        self._last_command = value

def append_string(S: str) -> str:
    global global_string
    if condition_programm.count_use_undo > 0:
        condition_programm.position = 0
        condition_programm.list_string_condition = [global_string, ]
        condition_programm.count_use_undo = 0
        condition_programm.count_use_append_or_del = 0

    condition_programm.append_to_string_condition(condition_programm.current_string_condition + S)
    condition_programm.position += 1
    condition_programm.last_command = 1
    condition_programm.count_use_append_or_del += 1

    global_string = condition_programm.current_string_condition
    return global_string


def del_symbols(N:str) -> str:
    global global_string
    N = int(N)

    if condition_programm.count_use_undo > 0:
        condition_programm.position = 0
        condition_programm.list_string_condition = [global_string, ]
        condition_programm.count_use_undo = 0
        condition_programm.count_use_append_or_del = 0

    if N >= len(global_string):
        condition_programm.append_to_string_condition("")
    else:
        condition_programm.append_to_string_condition(global_string[:-N])

    condition_programm.position += 1
    condition_programm.last_command = 2
    condition_programm.count_use_append_or_del += 1

    global_string = condition_programm.current_string_condition
    return global_string


def return_symbol_by_index(i:str) -> str:
    global global_string
    i = int(i)

    if i > len(global_string)-1:
        return ""
    return global_string[i]


def Undo():
    global global_string

    if condition_programm.last_command in (1, 2, 4, 5) and condition_programm.count_use_append_or_del > 0:
        condition_programm.position -= 1
        condition_programm.count_use_append_or_del -= 1
        global_string = condition_programm.current_string_condition
    condition_programm.last_command = 4
    condition_programm.count_use_undo += 1
    
    return global_string


def Redo():
    global global_string

    if condition_programm.last_command in (4, 5) and condition_programm.count_use_undo > 0:
        condition_programm.position += 1
        condition_programm.count_use_undo -= 1
        global_string = condition_programm.current_string_condition
        condition_programm.count_use_append_or_del += 1

    condition_programm.last_command = 5
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
condition_programm = ConditionProgrammList(["",],0, None)


