#import Modules
from tkinter import *
from tkinter.messagebox import askokcancel , askyesno
from requestHandle import GetData
from SettingWindow import Settings
import pandas as pd
import matplotlib.pyplot as plot
import Forecast , datetime
import os

#### exits files ####
if os.path.exists("Excel") == False:
    os.mkdir("Excel")
else:
    pass
#### varable ####
getdata = GetData()
settings = Settings()
window = Tk()

###### commands ######
def PISBINI():
    url=urltext_box.get()
    if getdata.check_url(url) == False:
        askokcancel("خطای 404","سایت مورد نظر یافت نشد")
    else:
        data=getdata.getURL(url)
        if data == False:
            askokcancel("خطای 505","سایت مورد نظر امکان وصل شدن به این برنامه را ندارد")
        else:
            sorter = getdata.SortJsonData(data)
            if sorter == False:
                askokcancel("خطای 501","داده های این سایت با این برنامه تناغظ دارد")
            else:
                sort  = sorter[0]
                for i in range(len(sort)):
                    forecast_mean = Forecast.nextYear(sort[i])
                    flag=askyesno("فایل اکسل","ایا تمایل به ذخیره ی اطلاعات دارید؟")
                    index=["Bahar","Tabestan","Pieeze","Zemestan"]
                    data = pd.DataFrame(forecast_mean,index=index)
                    data.plot.barh()
                    window.mainloop(1)
                    plot.show()
                    if flag:
                        data.to_excel("Excels/LevelRainFall"+"-"+ datetime.datetime().date().__str__())
                    else:
                        pass
                    exit(0)
                    
                    
        


#### config ####

window.geometry(settings.size)
window.title(settings.title)
window.resizable(settings.resizeable[0],settings.resizeable[1])

#### Elements ####
urltext_box = Entry(window,width=settings.width,border="3px")
button_send = Button(window,text="PISBINI",command=PISBINI)
urltext_box.pack()
button_send.pack()
window.mainloop()
