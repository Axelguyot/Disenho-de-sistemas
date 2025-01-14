from abc import ABC, abstractmethod
from passlib.hash import pbkdf2_sha256
from werkzeug.security import generate_password_hash, check_password_hash

class AbstractSecurity(ABC):

    @abstractmethod
    def encrypt_password(self, password:str) -> str:
        pass
    
    @abstractmethod
    def check_password(self, password_encrypted, plain_password) -> bool:
        pass

class WerkzeugSecurity(AbstractSecurity):
    
    def encrypt_password(self, password:str) -> str:
        password_encrypted = generate_password_hash(password)
        return password_encrypted
    
    def check_password(self, password_encrypted:str, plain_password:str) -> bool:
        return check_password_hash(password_encrypted, plain_password)

class PasslibSecurity(AbstractSecurity):
    
    def encrypt_password(self, password:str) -> str:
        return pbkdf2_sha256.hash(password)
        
    def check_password(self, password_encrypted:str, plain_password:str) -> bool:
        return pbkdf2_sha256.verify(plain_password, password_encrypted)