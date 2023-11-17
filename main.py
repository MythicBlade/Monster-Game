import Manager
from numpy import average
from time import perf_counter as pf
from DataHandler import Data

EPOCHS = 5
MAX_TURNS = 100
TREASURE_COUNT = 70
XDIM = 10
YDIM = 10


timeStart = pf()
m = Manager.Manager()
stats = m.trainAI(EPOCHS,0.8,1,0.995,0.2,MAX_TURNS,TREASURE_COUNT,XDIM,YDIM,monsterExists=False)
timeEnd = pf()

avg = average(stats)
print(f'The average is {avg}')
print(f'This process took {timeEnd-timeStart} seconds')
print(f'This process took {(timeEnd-timeStart)/60} minutes')
Data(stats,timeStart,timeEnd,EPOCHS,saveData=True,message='test_with_maybe_fixed_Qlearn3')




