import serial
import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig = plt.figure()

i = 0
x = []
y0 = []
y1 = []
y2 = []
y3 = []

i=0
ser = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600)
ser.close()
ser.open()

while True:
    data = ser.readline()
    print(data.decode())
    x.append(i)
    y0.append(data.decode()[0:5])
    y1.append(data.decode()[6:11])
    y2.append(data.decode()[12:17])
    y3.append(data.decode()[18:23])
    
    plt.scatter(i, float(data.decode()[0:5]),c='y')
    plt.scatter(i, float(data.decode()[6:11]),c='g')
    plt.scatter(i, float(data.decode()[12:17]),c='blue')
    plt.scatter(i, float(data.decode()[18:23]),c='black')
    
    
    i+=1
    plt.show()
    plt.pause(1)
    np.savetxt("results.csv", np.column_stack((x, y0, y1, y2, y3)), delimiter=",", fmt='%s')
    

