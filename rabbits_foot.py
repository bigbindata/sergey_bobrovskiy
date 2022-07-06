import math

def encode_string(s:str) -> str:
    
  clear_string = s.replace(" ","")
  length = len(clear_string)
  root = length**0.5
  n_columns = math.ceil(root)
  n_rows = math.floor(root)

  while length > n_rows * n_columns:
    n_rows += 1
  done_matrix = []

  for i in range(n_columns):
    if i == 0:
      done_matrix.append(clear_string[:n_rows])
    else:
      done_matrix.append(clear_string[n_rows*i:n_rows*(i+1)])

  done_list_string = []
  for i in range(len(done_matrix[0])):
    list_for_word = []
    for string in done_matrix:
      if len(string)-1 >= i:
        list_for_word.append(string[i])
    done_list_string.append("".join(list_for_word))

  return " ".join(done_list_string)


def decode_string(s:str) -> str:
  done_matrix = [[]]
  start_matrix_row = 0
  for i in s:
    if i == " ":
      done_matrix.append([])
      start_matrix_row += 1
    else:
      done_matrix[start_matrix_row].append(i)
  done_matrix
  list_for_word = []
  for i in range(len(done_matrix[0])):
    for list_symbols in done_matrix:
      if len(list_symbols)-1 >= i:
        list_for_word.append(list_symbols[i])

  return "".join(list_for_word)
  
def TheRabbitsFoot(s: str, encode: bool) -> str:
  if s == "":
    return ""
  if encode:
    return encode_string(s)
  else:
    return decode_string(s)