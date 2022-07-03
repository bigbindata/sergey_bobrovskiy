from typing import Tuple, List
import re
import copy

lenght = copy.deepcopy(len)
lenght

def return_new_word_with_space(word: str, N: int) -> str:
  new_list=[]
  for i in range(N,len(word), N):
    new_list.append(word[i-N: i])
  new_list.append(word[i:])
  return " ".join(new_list)

def return_new_string_with_spaces_and_list_index_space(string: str, N: int) -> Tuple[str,List[int]]:
  for word in string.split():
    if len(word) > N:
       string = string.replace(word, return_new_word_with_space(word, N))
  return string ,[m.start() for m in re.finditer(' ', string)]

def return_list_substring_with_space_for_replace_to_symbol_to_next_string(list_index_space: List[int], N: int):
  
  previous_checkpoint = 0
  list_substring_with_space = []
  for index, position in enumerate(list_index_space):
    if index == len(list_index_space)-1:
      list_substring_with_space.append(position)
      break
    if position - previous_checkpoint <= N+1:
      if list_index_space[index+1] - previous_checkpoint <= N+1:
        continue
      else:
        previous_checkpoint = position
        list_substring_with_space.append(previous_checkpoint)

  return list_substring_with_space

def return_code_is_string(string: str, word: str) -> List[int]:
  code_list_is_word_in_string = []
  for one_string in string.split("\n"):
    if re.search(f'(^| ){word}($| )', one_string):
      code_list_is_word_in_string.append(1)
    else:
      code_list_is_word_in_string.append(0)
  return code_list_is_word_in_string  

def WordSearch(len: int, s: str, subs: str) -> List[int]:
    
  new_string, list_index_space = return_new_string_with_spaces_and_list_index_space(s, len)
  list_substring_with_space = return_list_substring_with_space_for_replace_to_symbol_to_next_string(list_index_space, len)

  list_new_string = []
  for index in range(lenght(new_string)):
    if index in list_substring_with_space:
      list_new_string.append("\n")
    else:
      list_new_string.append(new_string[index])
  done_new_string = "".join(list_new_string)

  code_list_is_word_in_string = []
  for one_string in done_new_string.split("\n"):

    if re.search(f'(^| ){subs}($| )', one_string):
      code_list_is_word_in_string.append(1)
    else:
      code_list_is_word_in_string.append(0)
  return code_list_is_word_in_string