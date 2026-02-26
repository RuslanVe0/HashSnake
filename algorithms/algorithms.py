import hashlib
import bcrypt



def _encode(text, module) -> str:
    return module(text.encode("utf-8", errors = "ignore")).hexdigest()

class sha224():

    @staticmethod
    def _encode(text: str) -> str:
        return _encode(text, hashlib.sha224)

    @staticmethod
    def _compare(target_hash: str, word: str):
        return target_hash == word

    @staticmethod
    def __name__():
        return "sha224"

class sha1():

    @staticmethod
    def _encode(text: str) -> str:
        return _encode(text, hashlib.sha1)

    @staticmethod
    def _compare(target_hash: str, word: str):
        return target_hash == word

    @staticmethod
    def __name__():
        return "sha1"

class sha256():
    
    @staticmethod
    def _encode(text: str) -> str:
        return _encode(text, hashlib.sha256)

    @staticmethod
    def _compare(target_hash: str, word: str):
        return target_hash == word

    @staticmethod
    def __name__():
        return "sha256"
    
    
class md5():
    
    @staticmethod
    def _encode(text: str) -> str:
        return _encode(text, hashlib.md5)

    @staticmethod
    def _compare(target_hash: str, current_hash: str):
        return current_hash == target_hash

    @staticmethod
    def __name__():
        return "md5"
    
class sha512():

    @staticmethod
    def _encode(text: str) -> str:
        return _encode(text, hashlib.sha512)

    @staticmethod
    def _compare(target_hash: str, current_hash: str):
        return target_hash == current_hash

    @staticmethod
    def __name__():
        return "sha512"
    
class BCrypt():

    @staticmethod
    def _encode(text: str) -> str:
        return text.encode("utf-8", errors = "ignore")

    @staticmethod
    def _compare(target_hash: str, current_hash: str):
        return bcrypt.checkpw(target_hash.encode("utf-8", errors = "ignore"), current_hash)

    @staticmethod
    def __name__():
        return "BCrypt"