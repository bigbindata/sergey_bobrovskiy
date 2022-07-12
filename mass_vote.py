from typing import List

def MassVote(N:int, Votes:List[int]) -> str :
    max_voice = max(Votes)
    status = "majority"
    if Votes.count(max_voice) == 1:
        position = Votes.index(max_voice)+1
        if max_voice/sum(Votes) <= 0.5:
            status = "minority"
        return f"{status} winner {position}"
    
    return "no winner"