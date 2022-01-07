import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def visualisation(results,name,path): 
    plt.figure(1)
    plt.plot(results[:,0],results[:,1], 'y' , results[:,0], results[:,2], 'g' ,results[:,0],results[:,3], 'b' ,results[:,0],results[:,4], 'black')
    plt.ylim(20,30) #Chart range
    #plt.xlim(90,240)
    plt.grid()
    plt.title(name)
    plt.xlabel('Time [s]')
    plt.ylabel('Temperature [*C]')
    plt.legend(["Termistor 0","Termistor 1","Termistor 2","Termistor 3"])
    file_path = path.replace(".csv", ".png")
    plt.savefig(file_path)


def mean_velue(results):
    mean_1 = np.mean(results[:,1])
    mean_2 = np.mean(results[:,2])
    mean_3 = np.mean(results[:,3])
    mean_4 = np.mean(results[:,4])
    values = [mean_1, mean_2, mean_3, mean_4]
    values = np.round(values,2)
    return values

def max_velue(results):
    max_1 = np.max(results[:,1])
    max_2 = np.max(results[:,2])
    max_3 = np.max(results[:,3])
    max_4 = np.max(results[:,4])
    values = [max_1, max_2, max_3, max_4]
    return values

def statistic_values(mean_value, max_value, path):
    statistic_values = []
    statistic_values.append(mean_value)
    statistic_values.append(max_value)  
    file_path = path.replace(".csv", "_stat.csv")
    np.savetxt(file_path, np.column_stack((statistic_values)), delimiter=",", fmt='%s') 
    
if __name__ == "__main__":

    file_path = 'Results/flat_bar_basic/state/basic_state.csv'
    
    results = pd.read_csv(file_path, sep=',',header=None)
    results = pd.DataFrame(results).to_numpy()
    #results = results[90:240,:] #Range
    
    visualisation(results,"Temperatura kalibracji", file_path)
    
    statistic_values(mean_velue(results), max_velue(results), file_path)
    
    
    