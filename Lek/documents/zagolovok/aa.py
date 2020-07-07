import base64
from Crypto.Cipher import DES

enc = '2SHEXmvzAbFK0P6H5INLFEP2PLCC39CFE2YHTLQRN='
db = base64.decodebytes(enc.encode())
for i in range(100000, 999999):
    des = DES.new(str(i) + '00', DES.MODE_ECB)
    dc = des.decrypt(db)
    try:
        if ('=' in dc.decode()):
            print(dc)
    except:
        pass
