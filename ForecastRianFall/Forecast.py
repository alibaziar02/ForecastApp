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
    return ({"Level":means_pisbini}),
