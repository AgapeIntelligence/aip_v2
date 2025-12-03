#!/usr/bin/env python3
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
def encrypt_seed(seed:bytes,pw:bytes)->dict:
    key=HKDF(hashes.SHA256(),32,b"AIP_v2_salt_2025",b"agape-vault").derive(pw)
    n=os.urandom(12); c=AESGCM(key).encrypt(n,seed,None)
    return {"nonce":n.hex(),"ciphertext":c.hex()}
def decrypt_seed(e:dict,pw:bytes)->bytes:
    key=HKDF(hashes.SHA256(),32,b"AIP_v2_salt_2025",b"agape-vault").derive(pw)
    return AESGCM(key).decrypt(bytes.fromhex(e["nonce"]),bytes.fromhex(e["ciphertext"]),None)
