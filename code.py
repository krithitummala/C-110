import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random 

df = pd.read_csv("data.csv")
data = df["temp"].to_list()
population_mean = statistics.mean(data)
population_std = statistics.stdev(data)
fig = ff.create_distplot([data],["temp"], show_hist = False )
fig.add_trace(go.Scatter(x = [population_mean,population_mean], y = [0,1], mode = "lines", name = "mean"))
#fig.show()


print("The Population Mean is",population_mean)
print("The Population Standard Deviation is",population_std)

dataSet = []
for i in range(0,100):
    randomIndex = random.randint(0,len(data)-1)
    value = data[randomIndex]
    dataSet.append(value)

sampleMean = statistics.mean(dataSet)
sampleStd = statistics.stdev(dataSet)
print("The sample mean is", sampleMean)
print("The sample Standard Deviation is", sampleStd)

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"], show_hist= False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "mean"))
    fig.show()

def setup():
    meanList = []
    for i in range(0,1000):
        setOfMean = randomSetOfMean(100)
        meanList.append(setOfMean)
    showFig(meanList)
    calcMeanList = statistics.mean(meanList)
    calcStdList = statistics.stdev(meanList)
    print("The mean of the mean list is", calcMeanList)
    print("The standard deviation of the mean list is", calcStdList)
    
setup()
       