
"""import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {'country': ['A', 'B', 'C', 'D', 'E'],
         'gdp_per_capita': [45000, 42000, 52000, 49000, 47000]
         }
df1 = pd.DataFrame(data1)

data2 = {'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
         }
df2 = pd.DataFrame(data2)

data3 = {'interest_rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'index_price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
         }
df3 = pd.DataFrame(data3)

root = tk.Tk()

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['country', 'gdp_per_capita']].groupby('country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['year', 'unemployment_rate']].groupby('year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['interest_rate'], df3['index_price'], color='g')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['index_price'])
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Index Price')

root.mainloop()"""

import numpy as np

import matplotlib.pyplot as plot

# Get x values of the sine wave

time = np.arange(0, 12.8, 0.1)

# Amplitude of the sine wave is sine of a variable like time

amplitude = np.sin(time)
g = amplitude.copy()
a = len(amplitude)
#print(amplitude)
#print(a)
c_simple = []
for i in range(-1, a-1):
    #t.append(i)
    if amplitude[i] < 0.7 and amplitude[i]<amplitude[i+1]:
        amplitude[i] = 0
        c_simple.append(amplitude[i])
    elif amplitude[i]<0:
        amplitude[i] = 0
        c_simple.append(amplitude[i])
    else:
        c_simple.append(amplitude[i])

double = []
for i in g:
    if i<0:
        i = np.absolute(i)
        double.append(i)
    else:
        double.append(i)

z = double.copy()


c_double = []
for i in range(-1, a-1):
    #t.append(i)
    if z[i] < 0.7 and z[i]<z[i+1]:
        z[i] = 0
        c_double.append(z[i])
    else:
        c_double.append(z[i])




# Plot a sine wave using time and amplitude obtained for the sine wave
fig, (ax1, ax2, ax3, ax4) = plot.subplots(4)

ax1.plot(time, g)
ax2.plot(time, amplitude)
ax3.plot(time, double)
ax4.plot(time, c_double)
# Give a title for the sine wave plot

plot.title('Sine wave')

# Give x axis label for the sine wave plot

plot.xlabel('Time')

# Give y axis label for the sine wave plot

plot.ylabel('Amplitude = sin(time)')

plot.grid(True, which='both')

plot.axhline(y=0, color='k')

plot.show()