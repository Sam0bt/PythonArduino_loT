# PythonArduino_loT

Arduino kısmında bir led ve bir buzzer kullandım.

0 komutu kart led ve buzzer modullerine 5V verir.

1 komutu kart modulleri LOW moduna alır.

Pisi Linux üzerinde kodlanmıştır.

windows kullananlar:
ser=serial.Serial('/dev/ttyUSB0',9600, timeout=None) yerine;
serial.Serial('com7',9600) // com portu hangisi ise onu kullanmalıdır.


PySerial kütüphanesi kurulu ilave edilmelidir. Kurulu değilse;

python -m pip install pyserial

![fritzing](https://raw.githubusercontent.com/Sam0bt/LazarusArduino-loT/master/fritzing.png)

