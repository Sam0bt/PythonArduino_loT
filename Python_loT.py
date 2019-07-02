
import serial,sys
ser=serial.Serial('/dev/ttyUSB0',9600, timeout=None)
ser.flushInput()
char = raw_input("Komut Girin(0: ACIK/1: KAPALI) : ")
ser.write(char)
received =[]
ser.close()
