#VERY simple Caesar Cypher Encryption
def Encrypt(pin: str, key: int):
    PinValue = int(pin)
    PinValue += key
    if PinValue > 9999:
        PinValue -= 10000
    PinString=str(PinValue)
    while len(PinString)<4:
        PinString="0"+PinString
    return str(PinString)

