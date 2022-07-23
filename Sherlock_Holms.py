from collections import Counter
import copy


def is_dict_valid(test_dict:dict, key_valid:str) -> bool:
    dict_for_validate = copy.deepcopy(test_dict)

    if dict_for_validate[key_valid] - 1 == 0:
        dict_for_validate.pop(key_valid)
    else:
        dict_for_validate[key_valid] = test_dict[key_valid]-1

    if sum(dict_for_validate.values()) % len(dict_for_validate.values()) == 0 :
        return True
    return False

def SherlockValidString(s: str) -> bool:
    counter_dict = Counter (s)

    if len(set(counter_dict.values())) == 1 :
        return True

    most_common_value_key_in_string = Counter(counter_dict.values()).most_common(1)[0][0]

    for key, value in counter_dict.items():
        if value != most_common_value_key_in_string and is_dict_valid(counter_dict, key):
            return True
    return False