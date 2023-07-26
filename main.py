from stellar_sdk import xdr as stellar_xdr
from stellar_sdk.soroban.types import Struct, Bytes, Address

xdr = "AAAAEQAAAAEAAAADAAAADwAAAAZkYW9faWQAAAAAAA0AAAAERElWCgAAAA8AAAAIZGFvX25hbWUAAAANAAAAEkRlZXAgSW5rIFZlbnR1cmVzCgAAAAAADwAAAAhvd25lcl9pZAAAABIAAAAAAAAAACJh46WmZIVCyagaHEcOViSFxby24wtI2/ZVGzPVIScV"
sc_val = stellar_xdr.SCVal.from_xdr(xdr)

struct = Struct.from_xdr_sc_val(sc_val)

dao_id, dao_name, owner_id = struct.fields
print(f"{dao_id.key}={Bytes.from_xdr_sc_val(dao_id.value)}")
print(f"{dao_name.key}={Bytes.from_xdr_sc_val(dao_name.value)}")
print(f"{owner_id.key}={Address.from_xdr_sc_val(owner_id.value)}")
# dao_id=<Bytes [value=b'DIV\n']>
# dao_name=<Bytes [value=b'Deep Ink Ventures\n']>
# owner_id=<Address [type=ACCOUNT, address=GARGDY5FUZSIKQWJVANBYRYOKYSILRN4W3RQWSG36ZKRWM6VEETRLW6B]>

import binascii
address = Address.from_raw_contract(binascii.unhexlify("31ce07dca2fa5fd0dd90d1c84f21941bead4439d6fe6ac5a265bf1f819e04355"))
print(address)
# <Address [type=CONTRACT, address=CAY44B64UL5F7UG5SDI4QTZBSQN6VVCDTVX6NLC2EZN7D6AZ4BBVLMTZ]>