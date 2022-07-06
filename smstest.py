import serial
from time import sleep



ser = serial.Serial("/dev/ttyS0",
                    baudrate=115200,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=1
                    )

def send_at(command,ans,timeout,ser):
    
    ser.write(f'{command}\n'.encode())
    sleep(timeout)
    odpowiedz = ser.readlines()
    
    for x in odpowiedz:
        if ans in x.decode():
            return odpowiedz
        
b = send_at("AT+CSQ", "OK", 0.5, ser)


def csqsig(b_inna):
    print()
    for i in b_inna:
        if "CSQ:" in str(i):
            a = i[5:].decode()
            f = a.split(",")
    return f'Siła sygnału: {f[0]}'
        
#print(csqsig(b))
    
def wyslijsms(numer,wiadomosc,ser):
    numer = str(numer)
    send_at("at+CMFG=1","OK",3,ser)
    send_at(f'at+CMGS="{numer}"',"",3,ser)
    ser.write(f'{wiadomosc}\n'.encode())
    ser.write(bytes([26]))



    
        
    
