import time
import serial

ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
        c = input("Enter the character you want to send: ")
        char = c.encode()
        ser.write(char)
        time.sleep(0.05)
        if ser.inWaiting() > 0:
                character = ser.readline()
                s = character.decode()
                print(s)
                time.sleep(0.5)
        if ser.inWaiting() > 0:
                character = ser.readline()
                s = character.decode()
                print("The character received is {}".format(s))
                time.sleep(0.5)

