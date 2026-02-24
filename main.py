import os
import argparse
from algorithms.algorithms import md5, sha256, sha512, BCrypt
import HashSnake
import GUIApp


features: dict = {
    "md5": md5,
    "sha256" : sha256,
    "sha512": sha512,
    "BCrypt": BCrypt,
}

class CommandLine(object):
    
    
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog = "HashSnake", usage = "The purpose of this program is to compare hash values in order to find the original plaintext that corresponds to a given hash using a wordlist. This program is intended strictly for educational purposes.\
The authors of this program are not responsible for any misuse or damage caused by it.")
        
    def __repr__(self):
        return "CommandLine"
    
    def create_main_arguments(self):
        self.parser.add_argument("-t", "--target", help = "The user is required to provide target(s), e.g - --target=<hash1> or --target=<hash1>,<hash2>.")
        parser = self.parser.add_subparsers(dest = "command")
        self.add_parser(parser, "algorithms", "Choosing hashing algorithm", self.create_algorithms_argument)
        self.parser.add_argument("-w", "--wordlist", help = "Provide a wordlist.")
        self.parser.add_argument("-v", "--verbosity", help = "Verbosity debug", required = False, action = "store_true", default = False)
        self.parser.add_argument("-g", "--gui", help = "Turn on GUI interface", required = False, action = "store_true", default = False)
    def create_algorithms_argument(self, parser: object) -> None:
        parser.add_argument("-a", "--algorithm", choices = ["md5", "sha256", "sha512", "BCrypto", "all"], help = "Choose hasing algorithm")
    
    def add_parser(self, parser: argparse, name: str, description: str, function) -> None:
        function(parser.add_parser(name, help = description))
        
    
    def finalize(self):
        return self.parser.parse_args()
    
    
def start():
    
    _object: CommandLine = CommandLine()
    _object.create_main_arguments()
    parse_args = _object.finalize()
    if not parse_args.gui and not parse_args.target and not parse_args.algorithm and not parse_args.wordlist:
        raise ValueError("Invalid arguments provided.")
    elif parse_args.gui:
        GUIApp.GUIApp().start()
    target: list = []
    if "," in parse_args.target:
        target = parse_args.target.split(",")
    else:
        target.append(parse_args.target)
    if parse_args.algorithm not in features:
        raise ValueError("Invalid algorithm provided.")
    algorithm = features[parse_args.algorithm]
    wordlist = parse_args.wordlist
    if not os.path.exists(wordlist):
        raise OSError("Invalid directory provided. The path is not found.")
    HashSnake.HashSnake(target, algorithm.__call__(), wordlist, parse_args.verbosity, True).start()
    
    
if __name__ == "__main__":
    start()