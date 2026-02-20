import os
import argparse
from algorithms.algorithms import md5, sha256, sha512, BCrypt
import HashSnake


features: dict = {
    "md5": md5,
    "sha256" : sha256,
    "sha512": sha512,
    "BCrypt": BCrypt,
    "all": [md5, sha256, sha512, BCrypt]
}

class CommandLine(object):
    
    
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog = "HashSnake", usage = "The purpose of this program is to compare hash values in order to find the original plaintext that corresponds to a given hash using a wordlist. This program is intended strictly for educational purposes.\
The creator of this program is not responsible for any misuse or damage caused by it.")
        
    def __repr__(self):
        return "CommandLine"
    
    def create_main_arguments(self):
        self.parser.add_argument("-t", "--target", help = "The user is required to provide target(s), e.g - --target=<hash1> or --target=<hash1>,<hash2>.", required = True)
        parser = self.parser.add_subparsers(dest = "command", required = True)
        self.add_parser(parser, "algorithms", "Choosing hashing algorithm", self.create_algorithms_argument)
        self.parser.add_argument("-w", "--wordlist", help = "Provide a wordlist.", required = True)
        self.parser.add_argument("-v", "--verbosity", help = "Verbosity debug", required = False, action = "store_true", default = False)
    
    def create_algorithms_argument(self, parser: object) -> None:
        parser.add_argument("-a", "--algorithm", choices = ["md5", "sha256", "sha512", "BCrypto", "all"], required = True, help = "Choose hasing algorithm")
    
    def add_parser(self, parser: argparse, name: str, description: str, function) -> None:
        function(parser.add_parser(name, help = description))
        
    
    def finalize(self):
        return self.parser.parse_args()
    
    
def start():
    
    _object: CommandLine = CommandLine()
    _object.create_main_arguments()
    parse_args = _object.finalize()
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
    HashSnake.HashSnake(target, algorithm.__call__(), wordlist, parse_args.verbosity).start()
    
    
if __name__ == "__main__":
    start()