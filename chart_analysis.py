import pandas as pd
import matplotlib.pyplot as plt

state_data = pd.read_csv('Results/flat_bar_basic/state/basic_state.csv').to_numpy()
thermal_data = pd.read_csv('Results/flat_bar_basic/thermal/basic_1_thermal.csv').to_numpy()

plt.figure(1)
plt.plot(state_data[:, 1:5])
plt.xlabel('Time [s]')
plt.ylabel('Temperature [C]')
plt.grid()
plt.ylim(20, 60)
plt.figure(2)
plt.plot(thermal_data[:, 1:5])
plt.xlabel('Time [s]')
plt.ylabel('Temperature [C]')
plt.grid()
plt.ylim(20, 60)
plt.show()