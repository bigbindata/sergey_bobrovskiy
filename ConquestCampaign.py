from typing import List

def is_territory_capture(scan_territory):
    for i in scan_territory:
        if not all(i):
            return False
    return True

def return_index_capture_territory(scan_territory):
    dict_with_index_with_value_of_true={}
    for index, value in enumerate(scan_territory):
        if True in value:
            dict_with_index_with_value_of_true[index]=[]
            for sub_index, sub_value in enumerate(value):
                if sub_value == True:
                    dict_with_index_with_value_of_true[index].append(sub_index)
    return dict_with_index_with_value_of_true
  
def capture_territory(index_N,index_M,territory):
    try:
        territory[index_N+1][index_M]=True
    except:
        pass

    try:
        territory[index_N-1][index_M]=True
    except:
        pass

    try:
        territory[index_N][index_M+1]=True
    except:
        pass

    try:
        territory[index_N][index_M-1]=True
    except:
        pass

def ConquestCampaign(N: int, M: int, L: int, battalion: List[int])-> int:
    territory=[]
    number_day=1
    for _ in range(N):
        new_list = []
        for j in range(M):
          new_list.append(False)
        territory.append(new_list)
    for i in range(0,len(battalion),2):
        coordinata_N = battalion[i]
        coordinata_M = battalion[i+1]
        territory[coordinata_N-1][coordinata_M-1] = True
    while not is_territory_capture(territory):
        number_day+=1
        for index_N , list_index_M in return_index_capture_territory(territory).items():
            for index_M in list_index_M:
                capture_territory(index_N=index_N, index_M=index_M,territory=territory)

    return number_day
