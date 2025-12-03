#!/usr/bin/env python3
import argparse,json,getpass
from aip_core import generate_quantum_ris
from aip_identity import derive_identity
from aip_vault import encrypt_seed
p=argparse.ArgumentParser();p.add_argument("--generate",action="store_true");p.add_argument("--vault",action="store_true");a=p.parse_args()
if a.generate or a.vault:
    i=derive_identity(generate_quantum_ris()["quantum_spinor"])
    print(json.dumps({"version":"AIP-v2",**i},indent=2))
    if a.vault:
        pw=getpass.getpass("Vault password: ").encode()
        print(json.dumps(encrypt_seed(bytes.fromhex(i["ed25519_private_seed"]),pw),indent=2))
