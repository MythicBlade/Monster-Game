import matplotlib.pyplot as plt
import Manager
import numpy as np
from time import perf_counter as pf

EPOCHS = 100
MAX_TURNS = 120
TREASURE_COUNT = 75

def graph(inputs, saveFile = False):
    #make the x axis
    t = np.arange(0,len(inputs),step=1)
    
    #list of color palettes in format [axis, backround,bar]
    cool_color_palettes = ['#22223B','#C9ADA7','#4A4E69']
    warm_color_palettes = ['#6D6875', '#FFCDB2', '#E5989B']
     #choose actual color pallate from list above
    final_palette = cool_color_palettes
    axis_color = final_palette[0]
    backround_color = final_palette[1]
    bar_color = final_palette[2]
    # hide the toolbar and change axis color
    plt.rcParams['axes.edgecolor'] = axis_color
    plt.rcParams['toolbar'] = 'None'
    
    #make the graph
    fig = plt.figure(facecolor=backround_color)
    ax = plt.axes()
    ax.plot(t, stats)
    ax.grid(color=axis_color)
    #set colors
    ax.set_facecolor(backround_color)
    # naming the x-axis 
    plt.xlabel('Epoch',color = axis_color)
    # naming the y-axis
    plt.ylabel('Score',color = axis_color) 
    # plot title 
    plt.title('AI Stats!',color = axis_color) 
    

    
    #save the graph if the value for savefile is set
    if saveFile:
        fig.savefig(f"saves\\longtestwith75Treasure(6).png")
    plt.show()

    
time = pf()
m = Manager.Manager()
stats = m.trainAI(EPOCHS,1,1,0.9,0.2,MAX_TURNS,TREASURE_COUNT)

print(f'This process took {pf()-time} seconds')
graph(stats,saveFile=True)





