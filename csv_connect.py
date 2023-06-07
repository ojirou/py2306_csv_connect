import pandas as pd
import csv
import glob

sample_files = glob.glob('./sample_data/*.csv')
list = []
for file in sample_files:
    list.append(pd.read_csv(file))

    df = pd.concat(list)
    df.to_csv('./sample_data/marge_result.csv',index=False)
