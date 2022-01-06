import serial
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    
    plt.ion()
    fig = plt.figure()
    
    #Var
    i = 0
    x = []
    y0 = []
    y1 = []
    y2 = []
    y3 = []
    
    #data read from serial port
    ser = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600)
    ser.close()
    ser.open()
    
    while True:
        
        data = ser.readline()
        print(data.decode())
        
        #time
        x.append(i)
        #Temperature in Celsius from serial port
        y0.append(data.decode()[0:5])
        y1.append(data.decode()[6:11])
        y2.append(data.decode()[12:17])
        y3.append(data.decode()[18:23])
        
        #Live chart
        plt.scatter(i, float(data.decode()[0:5]),c='y')
        plt.scatter(i, float(data.decode()[6:11]),c='g')
        plt.scatter(i, float(data.decode()[12:17]),c='blue')
        plt.scatter(i, float(data.decode()[18:23]),c='black')
        
        i+=1
        plt.show()
        #Pause time 1 sec (same in arduino control program)
        plt.pause(1)
        
        #Saving results to csv file
        np.savetxt("results.csv", np.column_stack((x, y0, y1, y2, y3)), delimiter=",", fmt='%s')
    

