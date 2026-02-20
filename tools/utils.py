import threading
import time
import math
from collections import Counter


def threadedfunc(function):
    
    def wrapper(*args, **kwargs):
        
        threading.Thread(target = function, args = args, kwargs = kwargs).start()
    
    return wrapper


        
def calc(total_time: int):
    hours: int = int((total_time // 60) // 60)
    minutes: int = (total_time % 3600) // 60
    seconds: int = int(total_time % 60)
    if seconds < 10:
        seconds = f"0{int(seconds)}"
    return f"{hours}-hours:{int(minutes)}-minutes:{seconds}-seconds"


def calc_entropy(raw_text: str) -> int:
    length = len(raw_text)
    counts = Counter(raw_text)
    
    entropy: int = 0
    for count in counts.values():
        _p = (count / length)
        entropy -= _p * math.log2(_p)
        
    return entropy



class PList():
    
    
    def __init__(self, _list: list) -> None:
        self._list = _list
        self.size: int = 0
        
        
    def __repr__(self):
        return f"<PList _list={self._list}>"
    
    def next(self):
        if self.size > len(self._list)-1:
            return
        selected = self._list[self.size]
        self.size += 1
        return selected