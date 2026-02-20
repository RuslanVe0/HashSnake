import hashlib
import bcrypt


class sha256():
    
    
    def _encode(self, text: str) -> str:
        return hashlib.sha256(text.encode("utf-8", errors = "ignore")).hexdigest()
    
    def _compare(self, target_hash: str, word: str):
        return target_hash == word

    def __name__(self):
        return "sha256"
    
    
class md5():
    
    
    def _encode(self, text: str) -> str:
        return hashlib.md5(text.encode("utf-8", errors = "ignore")).hexdigest()
    
    def _compare(self, target_hash: str, current_hash: str):
        return current_hash == target_hash
    
    def __name__(self):
        return "md5"
    
class sha512():
    
    def _encode(self, text: str) -> str:
        return hashlib.sha512(text.encode("utf-8", errors = "ignore")).hexdigest()
    
    def _compare(self, target_hash: str, current_hash: str):
        return target_hash == current_hash
    
    def __name__(self):
        return "sha512"
    
class BCrypt():
    
    def _encode(self, text: str) -> str:
        return text.encode("utf-8", errors = "ignore")
    
    def _compare(self, target_hash: str, current_hash: str):
        return bcrypt.checkpw(target_hash.encode("utf-8", errors = "ignore"), current_hash)

    def __name__(self):
        return "BCrypt"