# Epic Title: Implement Data Encryption Protocols

import base64
import logging
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

class EncryptionService:
    BLOCK_SIZE = 16
    KEY = b'Sixteen byte key'  # AES needs a 16-byte key

    @staticmethod
    def encrypt(data: str) -> str:
        cipher = AES.new(EncryptionService.KEY, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), EncryptionService.BLOCK_SIZE))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        logging.info("Data encrypted successfully.")
        return iv + ct

    @staticmethod
    def decrypt(enc_data: str) -> str:
        try:
            iv = base64.b64decode(enc_data[:24])
            ct = base64.b64decode(enc_data[24:])
            cipher = AES.new(EncryptionService.KEY, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), EncryptionService.BLOCK_SIZE)
            return pt.decode('utf-8')
        except (ValueError, KeyError) as e:
            logging.error("Incorrect decryption")
            return ""