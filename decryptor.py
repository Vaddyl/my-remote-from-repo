from Crypto.Cipher import AES
import time
from hashlib import md5
from base64 import b64decode

tag = "Volga"
encrypted_flag = b64decode(b"uzF9t5fs3BC5MfPGe346gXrDmTIGGAIXJS88mZntUWoMn5fKYCxcVLmNjqwwHc2sCO3eFGGXY3cswMnO7OZXOw==")
start = 1585150500

# Bruteforce the key timestamp
for i in range(0,100000):
    key = md5(str(1585150500+i).encode("utf-8")).digest()
    aes = AES.new(key, AES.MODE_ECB)
    dec = aes.decrypt(encrypted_flag)
    if tag in str(dec):
        print(dec)
