from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

bKey = b""
bIvs = b""
sKey = ""
sIvs = ""

def create_mpg_aes_encrypt(data):
    cipher = AES.new(bKey, AES.MODE_CBC, iv=bIvs)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return ct_bytes.hex()

def create_mpg_sha_encrypt(data):
    plain_text = "HashKey=" + sKey + "&" + data + "&HashIV=" + sIvs
    m = hashlib.sha256()
    m.update(plain_text.encode())
    return m.hexdigest().upper()

def gen_query_string(data):
    new_string = ""
    for key, value in data.items():
        new_string += key + "=" + value + "&"
    new_string = new_string[:-1]
    return new_string