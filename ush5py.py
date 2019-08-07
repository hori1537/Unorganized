import sys
print(sys.path)
import os
import pandas as pd


df1 = pd.DataFrame([0,1])


from datetime import datetime

tdatetime = datetime.now()
foldername = 'result/'+ tdatetime.strftime('%Y%m%d-%H%M%S')
os.mkdir(foldername)

df1.to_csv( foldername + '/df1_2.csv')