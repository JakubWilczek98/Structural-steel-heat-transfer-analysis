import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def visualisation(results,name,path): 
    plt.figure(1)
    plt.plot(results[:,0],results[:,1], 'y' , results[:,0], results[:,2], 'g' ,results[:,0],results[:,3], 'b' ,results[:,0],results[:,4], 'black')
    plt.ylim(20,30)
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
    return mean_1, mean_2, mean_3, mean_4

if __name__ == "__main__":

    file_path = 'Results/flat_bar_basic/state/basic_state.csv'
    
    results = pd.read_csv(file_path, sep=',',header=None)
    results = pd.DataFrame(results).to_numpy()
    
    visualisation(results,"Temperatura kalibracji", file_path)
    
    print(mean_velue(results))
    