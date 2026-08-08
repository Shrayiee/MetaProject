import requests
import base64
import hashlib
import hmac
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def media_to_bytes(object):
    request = object[0]
    encryption_metadata = request["encryption_metadata"]
    cdn_url = request['cdn_url']
    aes_key = base64.b64decode(encryption_metadata["encryption_key"])
    hmac_key = base64.b64decode(encryption_metadata["hmac_key"])
    iv = base64.b64decode(encryption_metadata["iv"])
    expected_plaintext_hash = base64.b64decode(
        encryption_metadata["plaintext_hash"])
    expected_encrypted_hash = base64.b64decode(
        encryption_metadata["encrypted_hash"])
    response = requests.get(cdn_url)
    ciphertex = response.content
    # Then proceed with hash validation and decryption
    calculated_encrypted_hash = hashlib.sha256(ciphertex).digest()
    if calculated_encrypted_hash != expected_encrypted_hash:
        raise ValueError(
            "SHA256 hash of the encrypted file does not match the expected hash.")
    hmac_calculated = hmac.new(
        hmac_key, iv + ciphertex, hashlib.sha256).digest()


    hmac10 = hmac_calculated[:10]

    cipher = AES.new(aes_key, AES.MODE_CBC, iv)

    if len(ciphertex) % 16 != 0:
        ciphertex = ciphertex[:len(ciphertex) - (len(ciphertex) % 16)]
    decrypted_media_padded = cipher.decrypt(ciphertex)
    

    try:
        decrypted_media = unpad(decrypted_media_padded, AES.block_size)
        return base64.b64encode(decrypted_media).decode('utf-8')
    
    except ValueError:
        raise ValueError("Incorrect padding on decrypted media.")