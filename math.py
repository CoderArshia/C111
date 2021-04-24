import plotly.figure_factory as ff
import pandas as pd 
import csv
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_Score"].tolist()

# fig=ff.create_distplot([data],["math scores"],show_hist=False)
# fig.show()

# mean=statistics.mean(data)
# standard_deviation=statistics.stdev(data)

# print("mean is -->",mean)
# print("standard deviation is -->",standard_deviation)

def random_set(counter):
    dataSet=[]

    for i in range (0,counter):
       random_index=random.randint(0,len(data)-1)
       value=data[random_index]
       dataSet.append(value)

    mean=statistics.mean(dataSet)
    return mean

mean_list=[]

for i in range(0,1000):
    set_of_means=random_set(100)
    mean_list.append(set_of_means)

sd=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
# fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
# fig.show()

first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

df=pd.read_csv("data1.csv")
data=df["Math_Score"].tolist()

mean_of_sample1=statistics.mean(data)
print("mean of sample 1",mean_of_sample1)

fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE ONE"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION"))
fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_Score"].tolist()

mean_of_sample2=statistics.mean(data)
print("mean of sample 2",mean_of_sample2)

fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2,mean_of_sample2],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE ONE"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.show()

df=pd.read_csv("data3.csv")
data=df["Math_Score"].tolist()

mean_of_sample3=statistics.mean(data)
print("mean of sample 3",mean_of_sample3)

fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3,mean_of_sample3],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE ONE"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3"))
fig.show()

z_score=(mean_of_sample3-mean)/sd
print("the z score is -->",z_score)

z_score=(mean_of_sample2-mean)/sd
print("the z score is -->",z_score)

z_score=(mean_of_sample1-mean)/sd
print("the z score is -->",z_score)

