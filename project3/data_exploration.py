import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.cbook as cbook


df = pd.read_csv("graduates.csv")

newdf = df.head(n=10)

newdf.plot(kind='bar', x= 'Major', y ='Employed')
plt.xlabel("Major")
plt.ylabel("Employed")
newdf.plot(kind='bar', x= 'Major', y= "Layoff")
plt.xlabel("Major")
plt.ylabel("Laidoff")
newdf.plot(kind='bar', x = 'Major', y='Career Change')
plt.xlabel("Major")
plt.ylabel("Carreer Change(# of People)")
newdf.plot(kind ='scatter', x= "Managing/Supervising People/Projects", y="Males")
plt.xlabel("People in Manager Position")
plt.ylabel("Males")
newdf.plot(kind="line",y='Unemployed')

plt.show()
#fname = cbook.get_sample_data(df, asfileobj=False)
#fname2 =cbook.get_sample_data(df, asfileobj=False)


