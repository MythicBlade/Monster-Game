import matplotlib.pyplot as plt
from numpy import arange
from numpy import average
import csv

def Data(inputs, timeStart,timeEnd,EPOCHS,saveData = False,message = 'testofnetwork'):
    #get the test number from averages.csv
    with open('averages.csv','r+',newline='') as csvfile:
        last_entry = csvfile.readlines()[-1]
        num = int(last_entry.partition(',')[0]) + 1
        if saveData:
            write = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            write.writerow([num,EPOCHS,average(inputs),(timeEnd-timeStart)])
    
    #make the x axis
    t = arange(0,len(inputs),step=1)
    
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
    ax.plot(t, inputs)
    ax.grid(color=axis_color)
    #set colors
    ax.set_facecolor(backround_color)
    # naming the x-axis 
    plt.xlabel('Epoch',color = axis_color)
    # naming the y-axis
    plt.ylabel('Score',color = axis_color) 
    # plot title 
    plt.title('AI Stats!',color = axis_color) 
    
    #save the graph and the averages to csv if the value for saveData is set
    if saveData:
        fig.savefig(f"saves\\{message}({num}).png")
    
    plt.show()