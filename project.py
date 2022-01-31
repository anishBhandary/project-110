import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("p-data.csv")
data = df["reading_time"].to_list()
fig = ff.create_distplot([data],["reading_time"],show_hist = False)
fig.show()
print("population_mean",statistics.mean(data))

def random_data_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_figure(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines" ,name = "mean"))
    
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_data_mean(100)
        mean_list.append(set_of_mean)
        
    show_figure(mean_list)
    mean = statistics.mean(mean_list)

    print("Mean of the Sampling Distribution is",mean)

setup()

