import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path='C:/GitHub/crawl-and-analyze-marks/diemThiHaNoi.csv'
data=pd.read_csv(file_path)
data=data.drop(columns=['sbd'])
mean=data.mean()
median=data.median()
mode=data.mode().iloc[0]
variance=data.var()

print(f'Mean: {mean}\n Median: {median} \n mode: {mode} \n variance: {variance}')

data.hist(bins=5,figsize=(15,10))
plt.suptitle('histograme of exam scores')
plt.show()