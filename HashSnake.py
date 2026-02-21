import time
import re
import os
import tools.utils
from algorithms.algorithms import sha256, md5, BCrypt
import threading
import msvcrt

class HashEvent():
    
    
    _hash_string: str = ""
    _algorithm: str = None
    _dictionary: object = None
    _dictionary_size: int = 0
    _recovered: int = 0
    _status: bool = False
    _current_word: str = ""
    _current_hashed_word: str = ""
    _current_target: str = ""
    _path: str = ""
    _remaining_words: int = 0
    _speed: int = 0
    
    def load_path(self):
        for words in open(self._path, "r", encoding = "utf-8", errors = "ignore"):
            self._dictionary_size += 1
        self._remaining_words = self._dictionary_size

class TimerEvent():
    
    total_time: int = 0
    running: bool = True

def md5_check(target: str) -> str:
    size: int = 32
    if len(target) < size or len(target) > size:
        raise ValueError("It is required a MD5 hash.")
    if not re.fullmatch(r"[a-fA-F0-9]{32}", target):
        raise ValueError("It is required a MD5 hash.")
    
def sha256_check(target: str) -> str:
    size: int = 64
    if len(target) < size or len(target) > size:
        raise ValueError("It is required a SHA256 hash.")
    if not re.fullmatchtch(r"[a-fA-F0-9]{64}", target):
        raise ValueError("It is required a MD5 hash.")

def BCrypt_check(target: str) -> bool:
    if len(target.split(".")) < 2:
        raise ValueError("Salt is required.")

_TimerEvent = TimerEvent()

def get_agreement():
    return os.path.exists("agree.txt")

    
    
class HashSnake():

    functions: dict = {
        "md5": md5_check,
        "sha256": sha256_check,
        "BCrypt": BCrypt_check
    }

    def __init__(self, targets: list, algorithm: object, path: str, verbosity: bool, is_cli: bool = False) -> None:
        self.is_cli: bool = is_cli
        if self.is_cli and not get_agreement():
            print("\n\n[THIS MESSAGE WILL APPEAR ONCE!]\nThis program is intended to recover the plain-text value of a text. If used inappropriately to gain access to unauthorized system,\nthe authors of this project are not responsible.\n\n\nPress any key to continue.")
            msvcrt.getch()
            open("agree.txt", "a", encoding = "utf-8", errors = "ignore").write("User has agreed!")
        self.HashEvent = HashEvent()
        self.target_completion: int = 0
        self.HashEvent._hash_string = targets
        self.verbosity: bool = verbosity
        self.HashEvent._algorithm = algorithm
        for target in targets:
            self.functions[algorithm.__name__()].__call__(target)
        self.size_of_targets: int = len(targets)-1
        self.HashEvent._path = path
        self.HashEvent.load_path()
        self.counter: int = 0
            
        
    def __repr__(self):
        
        return f"<HashSnake hash_template={self.HashEvent}>"

    def compare_normal(self, words: str, targets: str):
        words = words.strip()
        clean_word: str = words
        words = self.HashEvent._algorithm._encode(words)
        if self.HashEvent._algorithm._compare(targets, words):
            self.HashEvent._recovered += 1
            with open("plain.txt", "a", encoding = "utf-8", errors = "ignore") as file:
                file.write(f"{targets}:{words} - {clean_word} - {tools.utils.calc(_TimerEvent.total_time)}\n")
            file.close()
            self.HashEvent._status = True
            self.system_clear()
            self.print_out()
    
    @staticmethod
    def system_clear():
        print("\033c", end = "")
    
    def print_out(self):
        if self.verbosity:
            print(f"""
-----------------------------------------------------------------
Current Hash ID (Job): {self.counter}
Session: {str(self.HashEvent._algorithm.__name__())}
Hash-Type: {str(self.HashEvent._algorithm.__name__())}
Wordlist path: {self.HashEvent._path}
Recovered: {self.HashEvent._recovered}/{len(self.HashEvent._hash_string)}
Total time elapsed: {tools.utils.calc(_TimerEvent.total_time)}
Speed: {self.HashEvent._speed} H/s
Estimated time: {tools.utils.calc(self.HashEvent._remaining_words / self.HashEvent._speed) if self.HashEvent._speed else "n/a"}
Completion rate: {(self.counter / self.HashEvent._dictionary_size)*100:.2f}%/100%
Target completion: {(self.target_completion / self.size_of_targets) * 100}%/100%

Words left: {self.HashEvent._remaining_words}/{self.HashEvent._dictionary_size}

Target: {self.HashEvent._current_target}


""")
    
    @tools.utils.threadedfunc
    def count_time(self):

        while _TimerEvent.running:
            _TimerEvent.total_time += 1
            self.system_clear()
            self.print_out()
            self._calc_speed()

    def _calc_speed(self):
        last_counter = self.counter
        time.sleep(1)
        current_counter: int = self.counter
        self.HashEvent._speed = current_counter - last_counter
    
    def start(self):
        _TimerEvent.running = True
        self.count_time()
        self.counter: int = 0
        try:
            for targets in self.HashEvent._hash_string:
                self.counter = 0
                self.HashEvent._current_target = targets
                self.HashEvent._status = False
                for words in open(self.HashEvent._path, encoding = "utf-8", errors = "ignore"):
                    if self.HashEvent._status:
                        break
                    if _TimerEvent.running:
                        self.compare_normal(words, targets)
                    self.counter += 1
                    self.HashEvent._remaining_words -= 1
                self.HashEvent._remaining_words = self.HashEvent._dictionary_size
                self.target_completion += 1
            _TimerEvent.running = False
            
        except KeyboardInterrupt:
            _TimerEvent.running = False
        
        except Exception as exception:
            print(f"Uh-oh, looks like an exception has been raised. Err: {exception}.")
            _TimerEvent.running = False

