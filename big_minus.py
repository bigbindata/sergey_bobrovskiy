from typing import Union, Tuple
from math import fabs

def minus_number(n1:Union[str, int], n2:Union[str, int]) -> Tuple[int] :
  result = int(n1) - int(n2)
  if result<0:
    return 1, 10+result
  return 0 , result

def BigMinus(s1: str, s2: str) -> str:
  if all((len(s1) == 1, len(s2) == 1)):
    return str(int(fabs(int(s1)-int(s2))))

  if len(s1) >= len(s2):
    long_string = s1
    short_string = s2   
  else:
    long_string = s2
    short_string = s1

  new_number = ""
  dop_number = 0
  for i in zip(short_string[::-1],long_string[::-1]):
    
    result = minus_number(i[1], int(i[0]) + dop_number)
    new_number += str(result[1])
    if result[0] == 1:
      dop_number = 1
    else:
      dop_number = 0

  new_number = new_number[::-1]

  length_new_number = len(new_number)

  if dop_number == 1:
    middle_str = ""
    for i in long_string[length_new_number-1::-1]:
      result = minus_number(i, 1)
      middle_str += str(result[1])
      if result[0] == 0:
        break
    done_string = long_string[:-length_new_number - len(middle_str)] + middle_str[::-1] + new_number
  else:
    done_string = long_string[:-length_new_number]+new_number
  return done_string
