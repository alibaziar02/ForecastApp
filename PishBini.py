import matplotlib.pyplot as plot
import pandas as pd
mizan_barandegi = [[20.5,10.5,5.1],[0.5,0.1,2],[5.5,10.25,22.25],[20.1,20.5,15.5]]
def mean(x:list) ->float:
    return sum(x) / len(x)
def nextYear(x:list):
    means = [mean(i) for i in x]
    pisbini=[]
    means_pisbini=[]
    for i in means:
        if i > 12.0:
            pisbini.append([x[means.index(i)][0] * 1.1,x[means.index(i)][1] * 1.1,x[means.index(i)][2]* 1.1])
        else:
            pisbini.append([x[means.index(i)][0] / 1.1,x[means.index(i)][1] / 1.1,x[means.index(i)][2] /1.1])
    means_pisbini = [mean(i) for i in pisbini]
    return ({"MIZAN":means_pisbini}),
